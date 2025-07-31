import mysql.connector

class DbTaskManager:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def __enter__(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            return self
        except mysql.connector.Error as err:
            raise ConnectionError(f"{err}.")
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
        except mysql.connector.Error as err:
            raise ConnectionError(f"{err}.")
        
    def db_create(self):
        try:
            with DbTaskManager(self.host, self.user, self.password, None) as db:
                db.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
                db.connection.commit()
                return True
        except mysql.connector.Error as err:
            raise ConnectionError(f"{err}.")
    
    def db_table_create(self):
        try:
            with DbTaskManager(self.host, self.user, self.password, self.database) as db:
                db.cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
	            id INT auto_increment PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                task VARCHAR(255) NOT NULL,
                state ENUM("not_initiated","in_progress","done") DEFAULT "not_initiated",
                date_of_creation DATETIME DEFAULT CURRENT_TIMESTAMP)
                """)
                db.connection.commit()
            return True
        except mysql.connector.Error as err:
            raise ConnectionError(f"{err}.")
    
    def db_add_task(self, name, task):
        try:
            with DbTaskManager(self.host, self.user, self.password, self.database) as db:
                sql = ("INSERT INTO tasks (name, task) VALUES (%s, %s)")
                values = (name, task)
                db.cursor.execute(sql, values)
                db.connection.commit()
            return db.cursor.rowcount > 0
        except mysql.connector.Error as err:
            raise ConnectionError(f"{err}.")

    def db_fetch_tasks_notdone(self):
        try:
            with DbTaskManager(self.host, self.user, self.password, self.database) as db:
                db.cursor.execute("SELECT * FROM tasks WHERE state IN ('not_initiated','in_progress')")
                return db.cursor.fetchall()
        except mysql.connector.Error as err:
            raise ConnectionError(f"{err}.")
    
    def db_fetch_tasks_all(self):
        try:
            with DbTaskManager(self.host, self.user, self.password, self.database) as db:
                db.cursor.execute("SELECT * FROM tasks")
                return db.cursor.fetchall()
        except mysql.connector.Error as err:
            raise ConnectionError(f"{err}.")

    def db_update_task(self, state, task_id):
        try:
            with DbTaskManager(self.host, self.user, self.password, self.database) as db:
                sql = "UPDATE tasks SET state = %s WHERE id = %s"
                values = (state, task_id)
                db.cursor.execute(sql, values)
                db.connection.commit()
                return db.cursor.rowcount > 0
        except mysql.connector.Error as err:
            raise ConnectionError(f"{err}.")

    def db_delete_task(self, task_id):
        try:
            with DbTaskManager(self.host, self.user, self.password, self.database) as db:
                sql = "SELECT name FROM tasks WHERE id = %s"
                db.cursor.execute(sql, (task_id,))
                result = db.cursor.fetchone()
                if result is None:
                    return None, False
                task_name = result[0]
                sql = "DELETE FROM tasks WHERE id = %s"
                db.cursor.execute(sql, (task_id,))
                db.connection.commit()
                success = db.cursor.rowcount > 0
                return task_name, success
        except mysql.connector.Error as err:
            raise ConnectionError(f"{err}.")