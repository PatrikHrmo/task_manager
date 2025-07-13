# Database connection
from db_connect import connection_db, initiation_db, table_creation
connection_db("localhost", "root", "1111", "")
initiation_db()
table_creation()


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


def tasks_enumerate():
    conn = connection_db("localhost", "root", "1111", "tasks")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    all_tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    number = len(all_tasks)
    return number


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


def update_task_db(task_id, state):
    conn = connection_db("localhost", "root", "1111", "tasks")
    cursor = conn.cursor()
    sql = "UPDATE tasks SET state = %s WHERE id = %s"
    values = (state, task_id)
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()


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


def delete_task_db(task_id):
    print(f"\nÚkol {task_id} byl odstraněn.")
    conn = connection_db("localhost", "root", "1111", "tasks")
    cursor = conn.cursor()
    sql = "DELETE FROM tasks WHERE id = %s"
    cursor.execute(sql, (task_id,))
    conn.commit()
    cursor.close()
    conn.close()


def end():
    print("\nKonec programu.")


main_menu()