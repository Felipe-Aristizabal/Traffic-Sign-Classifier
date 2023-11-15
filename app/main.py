import os
import time

from flask import Flask, render_template, Response, request, jsonify
from flask_socketio import SocketIO
from dotenv import load_dotenv
from flask_cors import CORS
import cv2

from utils.predict_images import preprocessing_images, load_predict_model
from db.mysql_connector import connectDB

# take environment variables from .env.
load_dotenv()

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
# Capture the default camera capture device
cap = cv2.VideoCapture(0)
socketio = SocketIO(app, cors_allowed_origins="*")

# Load the model that we want to use
model = load_predict_model()

last_frame = None


def predict_image(image):
    start_predict = time.time()

    predicts = (model.predict(image))
    # print(predicts)
    object_predited = None
    index_argMax = predicts.argmax()
    probability = predicts[0][index_argMax]
    print(probability)
    if (max(predicts[0]) < 0.98):
        print(" NO PREDIJO NADA")
    else:
        print(predicts.argmax())
        if (predicts.argmax() == 0):
            object_predited = "Speed"
        elif (predicts.argmax() == 1):
            object_predited = "Stop"
        elif (predicts.argmax() == 2):
            object_predited = "Traffic light"
        else:
            print("CLASIFFIER ERROR")
        # socketio.emit(
        #     "prediction", {"value": object_predited})
    end_predict = time.time()
    socketio.emit(
        "prediction", {"value": object_predited, "probability": float(probability), "timeToPredict": int(end_predict)})
    print(f"Time: {end_predict-start_predict} seconds")
    return object_predited


def capture_camera():
    global last_frame
    while True:
        ret, frame = cap.read()

        # Flip the camera
        frame = cv2.flip(frame, 1)

        # TODO: build the preprocessing here
        image = preprocessing_images(frame)

        # PREDICT IMAGE
        predict_image(image)

        (flag, encodedImage) = cv2.imencode(".jpg", frame)
        last_frame = frame
        if not flag:
            continue
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(encodedImage) + b'\r\n')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video_feed")
def video_feed():
    return Response(capture_camera(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")


@app.route("/validate/predict", methods=["POST"])
def validate_predict():
    global last_frame

    data = request.get_json()

    image = preprocessing_images(last_frame)
    result_classifier = predict_image(image)

    signal_by_user = data["id_selected"]
    name_by_user = data["name_selected"]
    correct_clasiffication = 0

    # ! COMPARAR SI LA ENTRADA DEL USUARIO Y EL PREDICTOR SON IGUALES
    if (name_by_user == result_classifier):
        correct_clasiffication = 1
    else:
        correct_clasiffication = 0

    # TODO: Save in BD
    con = connectDB()
    if con != None:
        cursor = con.cursor()
        result_classifier = cursor.execute(
            f"""INSERT INTO `register_classification` VALUES(default,%s,default, %s);""", (signal_by_user, correct_clasiffication))
        print(result_classifier)
        con.commit()
        cursor.close()
        con.close()

    else:
        print("NO hay una conexión")

    return jsonify(data)


if __name__ == "__main__":
    socketio.run(app=app, debug=True, port=os.getenv(
        "PORT"), host=os.getenv("HOST"))
