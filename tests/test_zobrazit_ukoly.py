import mysql.connector

# Pripojeni k databazi
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
        return None
    

# Zobrazi existujici ukol v databazi, jestli existuje
def test_zobrazit_ukoly():
    
    conn = pripojeni_db("localhost", "root", "1111", "ukoly")
    cursor = conn.cursor()
    
    cursor.execute("select * from ukoly;")
    vysledok = cursor.fetchall()

    cursor.close()
    conn.close()

    assert vysledok
