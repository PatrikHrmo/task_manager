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
def delete_task_db(task_id):
    if not task_id:
        raise ValueError
    else:
        conn = connection_db("localhost", "root", "1111", "tasks")
        cursor = conn.cursor()
        sql = "DELETE FROM tasks WHERE id = %s"
        cursor.execute(sql, (task_id,))
        deleted_rows = cursor.rowcount
        conn.commit()
        cursor.close()
        conn.close()
        print(f"\nÚkol {task_id} byl odstraněn.")
        return deleted_rows > 0


# Positive test: Deletes a row where id is equal to task_id.
@pytest.mark.positive
@pytest.mark.parametrize("task_id",
        [
            (3)
        ]
)

def test_delete_task_db_positive(task_id):
    conn = connection_db("localhost", "root", "1111", "tasks")
    cursor = conn.cursor()

    assert delete_task_db(task_id)

    cursor.close()
    conn.close()


# Negative test: The test passes when there is missing value of task_id, so nothing happens.
@pytest.mark.negative
@pytest.mark.parametrize("task_id",
        [
            ()
        ]
)

def test_delete_task_db_negative(task_id):
    conn = connection_db("localhost", "root", "1111", "tasks")
    cursor = conn.cursor()

    with pytest.raises(ValueError):
        delete_task_db(task_id)

    cursor.close()
    conn.close()