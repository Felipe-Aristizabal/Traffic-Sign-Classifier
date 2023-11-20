import os
import mysql.connector
from dotenv import load_dotenv

# Cargamos las variables de entorno del archivo .env
load_dotenv()


def connectDB():
    try:
        cnx = mysql.connector.connect(
            user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"), database=os.getenv("DB_DATABASE"),
            port=os.getenv("PORT_DB"))
        print("Conectado a DB")
        return cnx

    except ConnectionRefusedError:
        print(ConnectionRefusedError)
        print("Error en la conexión")
