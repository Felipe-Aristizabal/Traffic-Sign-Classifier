import os

from flask import Flask, render_template, Response, request, jsonify
from flask_socketio import SocketIO
from dotenv import load_dotenv
from flask_cors import CORS, cross_origin
import cv2

from utils.predict_images import preprocessing_images, load_predict_model, predict_image
from db.manipulate_data import insert_prediction_data, get_all_predictions_db

# Cargamos las variables de entorno del archivo .env
load_dotenv()

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Cargamos el modelo de clasificación que nosotros deseamos.
model = load_predict_model()
# Capturamos la entrada de video por defecto que posea el dispositivo.
cap = cv2.VideoCapture(0)
# En esta variable se almacenará el último frame que registre la cámara.
last_frame = None


def capture_camera():
    global last_frame
    while True:
        ret, frame = cap.read()

        # Inverimos la cámara en el eje x.
        frame = cv2.flip(frame, 1)
        # Realizamos el preprocesamiento a nuestra imagen actual
        image = preprocessing_images(frame)

        # Predecimos con nuestro modelo la imagen ya preprocesada.
        prediction_results = predict_image(image, model)

        socketio.emit(
            "prediction", prediction_results)
        print(f"Time: {prediction_results['timeToPredict']} seconds")

        (flag, encodedImage) = cv2.imencode(".jpg", frame)
        last_frame = frame
        if not flag:
            continue
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(encodedImage) + b'\r\n')


@app.route("/video_feed")
def video_feed():
    return Response(capture_camera(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")


@app.route("/validate/predict", methods=["POST"])
def validate_predict():
    global last_frame

    # Obtenemos la información mandada en el body de la petición POST.
    data = request.get_json()
    # Obtenemos la información del usuario enviada por el formulario. Exactamente, los valores de las clasves "signal_by_user" y "name_by_user"
    signal_by_user = data["id_selected"]
    name_by_user = data["name_selected"]

    # Realizamos el preprocesamiento y predicción de la última imagen guardada en la variable global.
    image = preprocessing_images(last_frame)
    result_classifier = predict_image(image, model)

    # Por defecto el clasificador tomará que el modelo no predijo bien
    correct_clasiffication = 0
    print(
        f"Dicho por el usuario: {signal_by_user} - Detectado por el modelo {result_classifier['value']}")

    # COMPARAR SI LA ENTRADA DEL USUARIO Y EL PREDICTOR SON IGUALES
    if (name_by_user == result_classifier["value"]):
        # Se almacenará en la BD que el clasificador hizo su labor correctamente.
        correct_clasiffication = 1
    else:
        # Se almancenará en la BD que el clasificador obtuvo un falso positivo.
        correct_clasiffication = 0

    new_data = insert_prediction_data(signal_by_user, correct_clasiffication)
    # Enviamos al cliente los nuevos datos actualizados.
    socketio.emit("insert-data", new_data)

    return jsonify(data)


@app.route("/predictions", methods=["GET"])
def get_data_db():
    # Obtenemos toda la información de la BD y la retonamos al usuario.
    all_predictions_db = get_all_predictions_db()
    return jsonify(all_predictions_db)


if __name__ == "__main__":
    socketio.run(app=app, debug=True, port=os.getenv(
        "PORT"), host=os.getenv("HOST"))
