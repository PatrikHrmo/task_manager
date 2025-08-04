# Db initiation
from db_connect import DbTaskManager

def setup_database():
    with DbTaskManager("localhost", "root", "1111", None) as conn:
        conn.db_create()
    with DbTaskManager("localhost", "root", "1111", "tasks") as conn:
        conn.db_table_create()


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
        with DbTaskManager("localhost", "root", "1111", "tasks") as conn:
            return conn.db_add_task(name, task)


# This function shows existing rows in the table. If not any, it prints a message.
def show_tasks_db():
    with DbTaskManager("localhost", "root", "1111", "tasks") as conn:
        individual_tasks = conn.db_fetch_tasks_notdone()
    if not individual_tasks:
        print("Nemáte žádné úkoly.")
    else:
        for i in individual_tasks:
            print(f"\n{i}")


# This function returns the number of all the rows in the table.
def tasks_enumerate():
    with DbTaskManager("localhost", "root", "1111", "tasks") as conn:
        all_tasks = conn.db_fetch_tasks_all()
    number = len(all_tasks)
    return number


# This function asks for a user import regarding the id of the task that the user wants to delete and the state that the user wants to assign to the task. Then it assigns the values to the variables task_id and state and returns them.
def update_task_import():
    while True:
        try:
            task_id = int(input("\nZadejte číslo úkolu, který si želáte aktualizovat: "))
        except ValueError:
            print("Špatná hodnota.")
            continue
        if task_id < 1:
            print("Špatné číslo.")
            continue
        break
    while True:
        try:
            choice = int(input("Želáte si přidelit nový stav? Pro stav PROBÍHÁ stiskněte 1, pro stav HOTOVO stiskněte 2: "))
        except ValueError:
            print("Špatná hodnota.")
            continue
        if choice < 1 or choice > 2:
            print("Špatná hodnota.")
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
        with DbTaskManager("localhost", "root", "1111", "tasks") as conn:
            result = conn.db_update_task(state, task_id)
        return result


# This function asks the user for an input of the number of the task that the user wishes to delete. Then it returns its value as task_id.
def delete_tasks_import(number):
    while True:
        try:
            task_id = int(input("\nZadejte číslo úkolu, který si želáte odstranit: "))
        except ValueError:
            print("Špatná hodnota.")
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
        with DbTaskManager("localhost", "root", "1111", "tasks") as conn:
            task_name, success = conn.db_delete_task(task_id)
        if success:
            print(f"\nÚkol {task_id} s názvom '{task_name}' byl odstraněn.")
        return success
    

# This function ends the program by printing the message.
def end():
    print("\nKonec programu.")


# Starting the app.
if __name__ == "__main__":
    setup_database()
    main_menu()