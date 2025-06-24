import mysql.connector

try:
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1111",
        database = "ukoly"
    )
except mysql.connector.Error as err:
    print(f"Chyba {err}.")