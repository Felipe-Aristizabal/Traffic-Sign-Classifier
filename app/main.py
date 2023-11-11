import os

from flask import Flask, render_template, Response
from dotenv import load_dotenv
import cv2

# take environment variables from .env.
load_dotenv()

# Indicate t
app = Flask(__name__)

# Capture the default camera capture device
cap = cv2.VideoCapture(0)


def capture_camera():
    while True:
        ret, frame = cap.read()
        # Flip the camera
        frame = cv2.flip(frame, 1)

        # TODO: build the preprocessing here
        (flag, encodedImage) = cv2.imencode(".jpg", frame)
        if not flag:
            continue
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(encodedImage) + b'\r\n')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cosa")
def index1():
    return Response("Hola")


@app.route("/video_feed")
def video_feed():
    return Response(capture_camera(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT"), host=os.getenv("HOST"))
