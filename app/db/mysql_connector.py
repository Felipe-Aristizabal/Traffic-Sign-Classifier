import mysql.connector


def connectDB():
    try:
        cnx = mysql.connector.connect(user='root', password='admin123',
                                      host='localhost',
                                      database='classifier',
                                      port=3306)
        print("Conectado a DB")
        return cnx

    except ConnectionRefusedError:
        print(ConnectionRefusedError)
        print("Error en la conexión")
