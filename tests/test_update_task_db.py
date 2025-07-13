import mysql.connector
import pytest

# Connection to the database
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

# Using of the database functions
connection_db("localhost", "root", "1111", "")
initiation_db()
table_creation()

# Tested function
def update_task_db(state, task_id):
    if not task_id or not state:
        raise ValueError
    else:
        conn = connection_db("localhost", "root", "1111", "tasks")
        cursor = conn.cursor()
        sql = "UPDATE tasks SET state = %s WHERE id = %s"
        values = (state, task_id)
        cursor.execute(sql, values)
        updated_rows = cursor.rowcount
        conn.commit()
        cursor.close()
        conn.close()
        return updated_rows > 0


# Positive test: The test changes the state from default to in_progress, and is successful if there is a task with id number 1.
@pytest.mark.positive
@pytest.mark.parametrize("state, task_id",
        [
            ("in_progress", 1)
        ]
)

def test_update_task_db_positive(state, task_id):
    conn = connection_db("localhost", "root", "1111", "tasks")
    cursor = conn.cursor()

    assert update_task_db(state, task_id)

    cursor.close()
    conn.close()


# Negative test: The test is successful if at least one of the values is empty: the state of the task is not updated.
@pytest.mark.negative
@pytest.mark.parametrize("state, task_id",
        [
            ("in_progress", 1)
        ]
)

def test_update_task_db_negative(state, task_id):
    conn = connection_db("localhost", "root", "1111", "tasks")
    cursor = conn.cursor()

    with pytest.raises(ValueError):
        update_task_db(state, task_id)

    cursor.close()
    conn.close()