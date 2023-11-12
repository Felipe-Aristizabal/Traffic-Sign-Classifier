import os
import time

from flask import Flask, render_template, Response
from flask_socketio import SocketIO
from dotenv import load_dotenv
from flask_cors import CORS
import cv2

from utils.predict_images import preprocessing_images, load_predict_model

# take environment variables from .env.
load_dotenv()

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
# Capture the default camera capture device
cap = cv2.VideoCapture(0)
socketio = SocketIO(app, cors_allowed_origins="*")


# Load the model that we want to use
model = load_predict_model()


def predict_image(image):
    start_predict = time.time()

    predicts = (model.predict(image))

    if (max(predicts[0]) < 0.5):
        print(" NO PREDIJO NADA")
    else:
        object_predited = None
        print(predicts.argmax())
        if (predicts.argmax() == 0):
            object_predited = "Speed"
        elif (predicts.argmax() == 1):
            object_predited = "Stop"
        elif (predicts.argmax() == 2):
            object_predited = "Traffic light"
        socketio.emit(
            "prediction", {"value": object_predited})
    end_predict = time.time()
    print(f"Time: {end_predict-start_predict} seconds")


def capture_camera():
    while True:
        ret, frame = cap.read()

        # Flip the camera
        frame = cv2.flip(frame, 1)

        # TODO: build the preprocessing here
        image = preprocessing_images(frame)

        # PREDICT IMAGE
        predict_image(image)

        (flag, encodedImage) = cv2.imencode(".jpg", frame)
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


if __name__ == "__main__":
    socketio.run(app=app, debug=True, port=os.getenv(
        "PORT"), host=os.getenv("HOST"))
