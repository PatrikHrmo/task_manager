import mysql.connector
import pytest

# Connection to the database.
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

# Initiation of the database, creating a database if it does not exist already.
def initiation_db():
    conn = connection_db("localhost", "root", "1111", "")
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS tasks")
    cursor.execute("USE tasks")
    cursor.close()
    conn.commit()
    conn.close()

# Creating a table if it does not exist already.
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

# Using of the database functions.
connection_db("localhost", "root", "1111", "")
initiation_db()
table_creation()


# Tested function:
def add_task_db(name, task):
    if not name or not task:
        raise ValueError("Toto pole je povinné.")
    else:
        conn = connection_db("localhost", "root", "1111", "tasks")
        cursor = conn.cursor()
        sql = ("INSERT INTO tasks (name, task) VALUES (%s, %s)")
        values  = (name, task)
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        return True


# Positive test: The test is successful if both name 1 and task 1 are added into the table.
@pytest.mark.positive
@pytest.mark.parametrize("name_1, task_1",
        [
            ("Name 1", "Task 1")
        ]
)

def test_add_task_db_positive(name_1, task_1):

    conn = connection_db("localhost", "root", "1111", "tasks")
    cursor = conn.cursor()

    assert add_task_db(name_1, task_1)

    cursor.close()
    conn.close()


# Negative test: The test is successful if at least one of the name 2 or task 2 is empty: nothing will be added into the table.
@pytest.mark.negative
@pytest.mark.parametrize("name_2, task_2",
        [
            ("Name 2", "")
        ]
)

def test_add_task_db_negative(name_2, task_2):
    conn = connection_db("localhost", "root", "1111", "tasks")
    cursor = conn.cursor()

    with pytest.raises(ValueError):
        add_task_db(name_2, task_2)

    cursor.close()
    conn.close()