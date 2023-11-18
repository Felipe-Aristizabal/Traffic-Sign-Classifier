from pathlib import Path
import time

import cv2
import numpy as np
from tensorflow.keras.models import load_model


def preprocessing_images(image):

    # resized_img = cv2.resize(image, (224, 224))
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
    if (max(predicts[0]) < 0.98):
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
        prediction_probability), "timeToPredict": int(end_predict-start_predict)}

    return prediction_results
