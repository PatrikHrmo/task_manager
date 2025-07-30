import mysql.connector

class DbTaskManager:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def db_connect(self, use_db=True):
        try:
            self.connection = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database if use_db else None
            )
            self.cursor = self.connection.cursor()
            return True
        except mysql.connector.Error as err:
            raise ConnectionError(f"{err}.")
        
    def db_create(self):
        if self.db_connect(use_db=False):
            try:
                self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
                self.connection.commit()
                self.db_close()
                return self.db_connect(use_db=True)
            except mysql.connector.Error as err:
                raise ConnectionError(f"{err}.")
        return False
    
    def db_table_create(self):
        self.db_connect()
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
	        id INT auto_increment PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            task VARCHAR(255) NOT NULL,
            state ENUM("not_initiated","in_progress","done") DEFAULT "not_initiated",
            date_of_creation DATETIME DEFAULT CURRENT_TIMESTAMP)
            """)
            self.connection.commit()
            return True
        except mysql.connector.Error as err:
            raise ConnectionError(f"{err}.")
              
    def db_close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        return True
    
    def db_add_task(self, name, task):
        self.db_connect()
        try:
            sql = ("INSERT INTO tasks (name, task) VALUES (%s, %s)")
            values = (name, task)
            self.cursor.execute(sql, values)
            self.connection.commit()
            return self.cursor.rowcount > 0
        except mysql.connector.Error as err:
            raise ConnectionError(f"{err}.")

    def db_fetch_tasks_notdone(self):
        self.db_connect()
        try:
            self.cursor.execute("SELECT * FROM tasks WHERE state IN ('not_initiated','in_progress')")
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            raise ConnectionError(f"{err}.")
    
    def db_fetch_tasks_all(self):
        self.db_connect()
        try:
            self.cursor.execute("SELECT * FROM tasks")
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            raise ConnectionError(f"{err}.")

    def db_update_task(self, state, task_id):
        self.db_connect()
        try:
            sql = "UPDATE tasks SET state = %s WHERE id = %s"
            values = (state, task_id)
            self.cursor.execute(sql, values)
            self.connection.commit()
            return self.cursor.rowcount > 0
        except mysql.connector.Error as err:
            raise ConnectionError(f"{err}.")

    def db_delete_task(self, task_id):
        self.db_connect()
        try:
            sql = "SELECT name FROM tasks WHERE id = %s"
            self.cursor.execute(sql, (task_id,))
            result = self.cursor.fetchone()
            if result is None:
                return None, False
            task_name = result[0]
            sql = "DELETE FROM tasks WHERE id = %s"
            self.cursor.execute(sql, (task_id,))
            self.connection.commit()
            success = self.cursor.rowcount > 0
            return task_name, success
        except mysql.connector.Error as err:
            raise ConnectionError(f"{err}.")