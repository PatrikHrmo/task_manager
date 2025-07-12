import mysql.connector

def connection_db(host,user,password,database):

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
    
def initiation_db():
    conn = connection_db("localhost", "root", "1111", "")
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS tasks")
    cursor.execute("USE tasks")
    cursor.close()
    conn.commit()
    conn.close()

def table_creation():
    conn = connection_db("localhost", "root", "1111", "tasks")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
	id INT auto_increment PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    task VARCHAR(255) NOT NULL,
    state ENUM("not_initiated","in_progress","done") DEFAULT "not_initiated",
    date_of_creation DATETIME DEFAULT CURRENT_TIMESTAMP)
""")
    cursor.close()
    conn.commit()
    conn.close()

connection_db("localhost", "root", "1111", "")
initiation_db()
table_creation()

# Zobrazi existujici ukol v databazi, jestli existuje
def test_show_tasks():
    
    conn = connection_db("localhost", "root", "1111", "tasks")
    cursor = conn.cursor()
    cursor.execute("select * from tasks;")
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    if result:
        assert "Úlohy existujú."
    else:
        assert "Úlohy neexistujú."