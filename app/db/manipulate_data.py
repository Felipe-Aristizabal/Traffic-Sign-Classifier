from db.mysql_connector import connectDB


def get_all_predictions_db():
    con = connectDB()
    if con != None:
        cursor = con.cursor()
        # Obtenemos todos los registros de la base de datos de la siguiente manera:
        # [id_señal, suma de las predicciones correctas, total de predicciones registradas]
        cursor.execute(
            f"""SELECT rc.signal_id,s.signal_name,  SUM(correct_predict = 1) AS num_correct_predictions,
            COUNT(rc.signal_id) AS total_signals FROM register_classification as rc 
            INNER JOIN signals as s ON s.signal_id = rc.signal_id GROUP BY rc.signal_id ;""")
        records = cursor.fetchall()

        # El arreglo resultante del método fetchall() lo convertimos en un solo arreglo
        # con varios diccionarios, iterándose por medio de un for.
        json_list = [
            {
                'signal_id': item[0],
                'signal_name': item[1],
                'totalCorrectPredictions': int(item[2]),
                'totalPredictions': item[3]
            } for item in records
        ]
        cursor.close()
        # Cerramos la conexión a la BD.
        con.close()
        return json_list
    else:
        raise Exception("ERROR: NO hay una conexión a la BD.")


def insert_prediction_data(signal_by_user, correct_clasiffication):
    con = connectDB()
    if con != None:
        cursor = con.cursor()
        # Insertamos en la BD el valor seleccionado por el usuario en el cliente y si la predicción del modelo acertó con lo que dijo el usuario.
        result_classifier = cursor.execute(
            f"""INSERT INTO `register_classification` VALUES(default,%s,default, %s);""", (signal_by_user, correct_clasiffication))
        # print(result_classifier)
        # Guardamos los resultamos en la BD con commit()
        con.commit()
        cursor.close()
        con.close()

        # Obtenemos todos los registros junto con el nuevo valor insertado.
        all_predictions_db = get_all_predictions_db()
        return all_predictions_db
    else:
        raise Exception("ERROR: NO hay una conexión a la BD.")
