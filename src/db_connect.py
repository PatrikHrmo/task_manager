import mysql.connector

def pripojeni_db(host,user,password,database):

    try:
        conn = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Chyba {err}.")