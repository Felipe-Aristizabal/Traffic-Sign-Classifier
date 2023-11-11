import time
import os
from pathlib import Path

import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

cap = cv2.VideoCapture(0)

# Obtener el directorio actual (donde se encuentra test-model.py)
current_directory = Path.cwd()

# Construir la ruta hacia first-model.h5
model_path = current_directory / 'app' / 'models' / 'first-model.h5'

model_test = load_model(model_path)
# print(model_test.summary())
labels = ["Speed", "Stop", "Traffic light"]


def predict_melo(frame):

    resized_img = cv2.resize(frame, (150, 150))
    normalized_img = resized_img / 255.0
    good_image = np.reshape(normalized_img, (1, 150, 150, 3))

    start_predict = time.time()
    predicts = (model_test.predict(good_image))

    if (max(predicts[0]) < 0.5):
        print(" NO PREDIJO NI MONDÁ")
    else:
        print(predicts.argmax())
    end_predict = time.time()
    print(f"Time: {end_predict-start_predict} seconds")


if __name__ == "__main__":

    while cap.isOpened():
        _, frame = cap.read()
        key = cv2.waitKey(1)
        # Reducimos el tamaño de la imagen para disminuir el costo de computo
        frame = cv2.resize(
            frame, (int(frame.shape[1]/2), int(frame.shape[0]/2)))

        frame = cv2.flip(frame, 1)

        cv2.imshow("Result", frame)

        print("Predicción: ")
        predict_melo(frame)
        print("--------------------------------------")
