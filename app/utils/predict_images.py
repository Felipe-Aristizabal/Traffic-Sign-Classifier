from pathlib import Path

import cv2
import numpy as np
from tensorflow.keras.models import load_model


def preprocessing_images(image):

    resized_img = cv2.resize(image, (224, 224))
    resized_img = cv2.resize(image, (299, 299))
    # resized_img = cv2.resize(image, (150, 150))
    # Normalize the pixel values since 0 to 255
    normalized_img = resized_img / 255.0
    # Convert image to tensor
    tensor_img = np.reshape(normalized_img, (1, 299, 299, 3))
    return tensor_img


def load_predict_model():
    # Obtener el directorio actual (donde se encuentra test-model.py)
    current_directory = Path.cwd()

    # Construir la ruta hacia first-model.h5
    # model_path = current_directory / 'app' / 'models' / 'first-model.h5'

    model_path = current_directory / 'app' / \
        'models' / 'best_modelV3_TL.h5'
    # Construir la ruta hacia first-model.h5
    # model_path = current_directory / 'app' / \
    #     'models' / 'best_modelV3_TL-mobileNet.h5'

    model_test = load_model(model_path)
    return model_test
#  while cap.isOpened():
#         _, frame = cap.read()
#         key = cv2.waitKey(1)
#         # Reducimos el tamaño de la imagen para disminuir el costo de computo
#         frame = cv2.resize(
#             frame, (int(frame.shape[1]/2), int(frame.shape[0]/2)))

#         frame = cv2.flip(frame, 1)

#         cv2.imshow("Result", frame)

#         print("Predicción: ")
#         predict_melo(frame)
#         print("--------------------------------------")
