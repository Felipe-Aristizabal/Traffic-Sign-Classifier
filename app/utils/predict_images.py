from pathlib import Path
import time

import cv2
import numpy as np
from tensorflow.keras.models import load_model


def preprocessing_images(image):

    # Reescalamos la imagen de acuerdo con las indicaciones de la arquitectura de CNN escogida
    resized_img = cv2.resize(image, (224, 224))
    # Normalizamos los valores de los pixeles de 0 a 1, puesto que 255 es el mayor valor de intensidad que nuestra imagen es 255.
    normalized_img = resized_img / 255.0
    # Convertimos nuetra imagen a tensor. Esta será nuestra entrada para el modelo entrenado.
    tensor_img = np.reshape(normalized_img, (1, 224, 224, 3))
    return tensor_img


def load_predict_model():
    # Obtener el directorio actual (donde se encuentra test-model.py)
    current_directory = Path.cwd()

    # Construir la ruta hacia first-model.h5
    model_path = current_directory / 'app' / \
        'models' / 'VGG16_v1.h5'

    model_test = load_model(model_path)
    return model_test


def predict_image(image, model):
    object_predited = None

    # Calculamos el tiempo que se demora en predecir.
    start_predict = time.time()
    # Predecimos la imagen pasada por parámetro con nuetro modelo.
    predicts = (model.predict(image))
    end_predict = time.time()

    index_argMax = predicts.argmax()
    prediction_probability = predicts[0][index_argMax]

    # Si ninguna de los porcentajes de predicción superan el 0.98, asumiremos que en la imagen no se muestra ninguna de las señales de tránsito disponibles en el modelo.
    if (max(predicts[0]) < 0.90):
        # print(" NO PREDIJO NADA")
        pass
    else:
        # print(predicts.argmax())
        if (predicts.argmax() == 0):
            object_predited = "Speed"
        elif (predicts.argmax() == 1):
            object_predited = "Stop"
        elif (predicts.argmax() == 2):
            object_predited = "Traffic light"
        else:
            # print("CLASIFFIER ERROR")
            pass

    # Retornaremos toda la información del resultado del modelo en un diccionario para que sea más legible.
    prediction_results = {"value": object_predited, "probability": float(
        prediction_probability), "timeToPredict": float(end_predict-start_predict)}

    return prediction_results
