# Database connection
from db_connect import connection_db, initiation_db, table_creation
connection_db("localhost", "root", "1111", "")
initiation_db()
table_creation()


# Main menu function. This function prints the main menu and returns it when there is a faulty imput or when a block of functions ends. The program when the input is equal to 5.
def main_menu():
    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Aktualizovat úkol.")
        print("4. Odstranit úkol")
        print("5. Konec programu")

        try:
            option = int(input("\nVyberte možnost (1-5): "))
        except ValueError:
            print("Špatné číslo.")
            continue
        if option < 1 or option > 5:
            continue

        if option == 1:
            name, task = add_task_import()
            add_task_db(name, task)
        elif option == 2:
            show_tasks_db()
        elif option ==3:
            show_tasks_db()
            number = tasks_enumerate()
            if number == 0:
                print("Nemáte žádné úkoly.")
                continue
            task_id, state = update_task_import()
            update_task_db(task_id, state)
        elif option == 4:
            show_tasks_db()
            number = tasks_enumerate()
            if number == 0:
                print("Nemáte žádné úkoly.")
                continue
            task_id = delete_tasks_import(number)
            delete_task_db(task_id)
        elif option == 5:
            end()
            break      


# This function serves to ask for user input and stores it into the variables name and task.
def add_task_import():
    while True:
        name = input("\nZadejte název úkolu: ")
        if name == "":
            continue
        break
    while True:
        task = input("Zadejte popis úkolu: ")
        if task == "":
            continue
        break
    return name, task


# This function stores the variables name and task into the values name and task in the table, and returns True if successful.
def add_task_db(name, task):
    if not name or not task:
        raise ValueError
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


# This function shows existing rows in the table. If not any, it prints a message.
def show_tasks_db():
    conn = connection_db("localhost", "root", "1111", "tasks")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE state IN ('not_initiated','in_progress');")
    individual_tasks = cursor.fetchall()
    if not individual_tasks:
        print("Nemáte žádné úkoly.")
    else:
        for i in individual_tasks:
            print(f"\n{i}")
    cursor.close()
    conn.close()


# This function returns the number of all the rows in the table.
def tasks_enumerate():
    conn = connection_db("localhost", "root", "1111", "tasks")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    all_tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    number = len(all_tasks)
    return number


# This function asks for a user import regarding the id of the task that the user wants to delete and the state that the user wants to assign to the task. Then it assigns the values to the variables task_id and state and returns them.
def update_task_import():
    while True:
        try:
            task_id = int(input("\nZadejte číslo úkolu, který si želáte aktualizovat: "))
        except ValueError:
            continue
        if task_id < 1:
            print("Špatné číslo.")
            continue
        break
    while True:
        try:
            choice = int(input("Želáte si přidelit nový stav? Pro stav PROBÍHÁ stiskněte 1, pro stav HOTOVO stiskněte 2: "))
        except ValueError:
            continue
        if choice < 1 or choice > 2:
            continue
        elif choice == 1:
            state = "in_progress"
        elif choice == 2:
            state = "done"
        break
    return task_id, state


# This function updates the table with the variables task_id and states and stores them under the columns task_id and state, and returns True when done.
def update_task_db(task_id, state):
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


# This function asks the user for an input of the number of the task that the user wishes to delete. Then it returns its value as task_id.
def delete_tasks_import(number):
    while True:
        try:
            task_id = int(input("\nZadejte číslo úkolu, který si želáte odstranit: "))
        except ValueError:
            continue
        if task_id < 1:
            print("Špatné číslo.")
            continue
        break
    return task_id


# This function takes the value of task_id and uses it to identify the id in the table and delete the relative row. When done, it returns True.
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

# This function ends the program by printing the message.
def end():
    print("\nKonec programu.")


main_menu()