import mysql.connector
import pytest
from src.main import add_task_db

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


# The test passes if there are tasks. It fails if there are no tasks.
def test_show_tasks_exist():
    
    conn = connection_db("localhost", "root", "1111", "tasks")
    cursor = conn.cursor()
    cursor.execute("select * from tasks;")
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    assert result != [], "There are existing tasks."
    print("There are existing tasks.")


# The test passes if there are no tasks. It fails if there are tasks.
def test_show_tasks_noexist():

    conn = connection_db("localhost", "root", "1111", "tasks")
    cursor = conn.cursor()
    cursor.execute("select * from tasks;")
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    assert result == [], "There are no tasks."
    print("There are no tasks.")


@pytest.mark.parametrize("name_1, task_1", 
        [
            ("Task 1", "Description 1"),
        ]
)


def test_add_task_db_positive(name_1, task_1):
    conn = connection_db("localhost", "root", "1111", "tasks")
    cursor = conn.cursor()
    sql = ("INSERT INTO tasks (name, task) VALUES (%s, %s)")
    values  = (name_1, task_1)
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()

    assert cursor.rowcount == 1, "The task has been added successfuly."
    print("The task has been added successfuly.")


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