# Traffic-Sign-Classifier

The model used for traffic signal classification named `ModelV3_InceptionV3.h5` can be found at the [following link](https://uao-my.sharepoint.com/:f:/g/personal/hector_fabio_romero_uao_edu_co/Eq6wNtHNeXtIqw-1CjkkI8EBiJf4wdLm455Gt4VAZHaJ1Q?e=WaZcCi).

## Team Members

-   [Andrés Felipe Aristizábal Miranda](https://github.com/Felipe-Aristizabal)
-   [Andrés Bonilla Galindo](https://github.com/AndresBonilla0306)
-   [Hector Fabio Romero Bocanegra](https://github.com/Hector-f-Romero)

## Overview

-   [Introduction and Problem Description](#introduction-and-problem-description)
-   [Getting Started](#getting-started)
-   [Machine Learning Problem](#machine-learning-problem)
-   [Data Collection and Preprocessing Methodology](#data-collection-and-preprocessing-methodology)
-   [Deployment Architecture Selection](#deployment-architecture-selection)
-   [Flask Application Description and Functionality](#flask-application-description-and-functionality)
-   [Datasets](#flask-application-description-and-functionality)

## Introduction and Problem Description

In Colombia, road safety education is crucial for all ages. This project, in the field of Digital Image Processing, introduces a necessary tool to promote basic traffic signal knowledge among younger generations, specifically fifth graders in Santiago de Cali schools. The traffic signal classification system employs advanced technology for real-time detection and information provision, aiding children and their families in making safe road decisions.

The team aims to develop a real-time image classifier for traffic signals throughout Santiago de Cali, capable of recognizing stop, speed, and traffic light signals under good daylight conditions. This will be achieved using Python and deployed locally on a web application, allowing end-users to utilize this tool without downloading external applications. Additionally, a MySQL database will record the classifier model's results for subsequent analysis and visualization.

## Getting Started - Backend

1. Clone the branch `main` [here](https://github.com/Felipe-Aristizabal/Traffic-Sign-Classifier)
2. Configure the MySQL user and run the script `database-config-start.sql`
3. Download the model `ModelV3_InceptionV3.h5` in the next [link](https://uao-my.sharepoint.com/:f:/r/personal/andres_aristizabal_m_uao_edu_co/Documents/7.%20S%C3%A9ptimo%20semestre/PDI/Modelos/Traffic%20Signal%20recognition?csf=1&web=1&e=qfQNDn). Put the file in the route `models`.
4. Install `virtualenv` to management the version of the libraries with `pip install virtualenv`.
5. Create a virtual enviroment with `python -m virtualenv env`.
6. Run `.\env\Scripts\activate` to active the virtual enviroment.
7. Run `pip install -r "requirements.txt"` to install all the libraries used with the specific version.
8. Create a `.env` file inside the `app` folder. Configure the enviroment variables in: `HOST, PORT, DB_USER, DB_PASSWORD, DB_HOST, DB_DATABASE, PORT_DB`.
9. Execute the project in `frontend` branch. To configure this part, look its `README.md` in that [branch](https://github.com/Felipe-Aristizabal/Traffic-Sign-Classifier/tree/frontend).
10. Run in terminal `python .\app\main.py`

## Machine Learning Problem

The machine learning challenge involves creating a video image classifier to identify three key elements: traffic lights, stop signs, and speed limit signs accurately and efficiently. The intention is to develop a robust model for classroom use to help fifth graders differentiate traffic signals by experimenting with three different neural network architectures:

1. Custom architecture based on existing solutions, tailored specifically for the dataset's unique characteristics.
2. Pre-established and proven architecture like VGG16, which provides a valuable baseline for comparison.
3. Transfer learning implementation with an advanced network such as InceptionV3, utilizing pre-trained weights to specialize in traffic signal classification.

The final goal is to compare these architectures to determine which provides the best precision, speed, and generalization for the task of classifying traffic images, as the trained model will be deployed on the web for real-time use.

## Data Collection and Preprocessing Methodology

Data was collected through a mixed process of direct capture and sourcing from public databases. Initially, 125 images for each category (traffic lights, stop signs, and speed limits) were captured to ensure variability in lighting, viewing angles, and backgrounds, reflecting real-world conditions for better model generalization. To augment this dataset, 75 additional images per category were sourced from Roboflow and Kaggle, resulting in 200 images per category. These external sources were crucial for enriching the dataset and facilitating a more robust training and accurate model evaluation.

## Deployment Architecture Selection

After evaluating compiled models, the team opted for the transfer learning model due to its superior performance in real-time detection with a virtual camera, demonstrating exceptional precision of 95% for images captured within 20cm of the camera. The transfer learning model had significantly more trainable parameters, which allowed for greater classification accuracy.

## Flask Application Description and Functionality

A Flask server was developed to interact with a web page as required by the project. It supports real-time communication to relay the classifier's results while capturing images from the camera. The server utilizes websockets for bidirectional communication and implements CORS for secure cross-origin resource sharing.

## Datasets

The datasets used for this project were sourced from a combination of proprietary collection and public databases to ensure a balanced and representative dataset for training the model. The following datasets were specifically used:

-   Traffic Sign Dataset found on Roboflow with CC BY 4.0 license, which can be consulted at this [link](https://public.roboflow.com/object-detection/traffic-sign).
-   Road Sign Detection found on Kaggle with a CC0 license, which can be accessed at this [link](https://www.kaggle.com/andrewmvd/road-sign-detection).

These external sources were fundamental in enriching the dataset and facilitating robust training and precise evaluation of the traffic signal classification model.
