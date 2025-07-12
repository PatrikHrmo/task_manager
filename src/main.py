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
        print("3. Odstranit úkol")
        print("4. Konec programu")

        try:
            option = int(input("Vyberte možnost (1-4): "))
        except ValueError:
            continue
        if option < 1 or option > 4:
            continue

        if option == 1:
            name, task = add_task_import()
            add_task_db(name, task)
            call_task(name, task)
        elif option == 2:
            show_tasks()
        elif option == 3:
            add_task_db()
        elif option == 4:
            end()
            break      


def add_task_import():
    while True:
        name = input("Zadejte název úkolu: ")
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
    if name == "":
        return None
    if task == "":
        return None
    else:
        conn = connection_db("localhost", "root", "1111", "tasks")
        cursor = conn.cursor()
        sql = ("INSERT INTO ukoly (name, task) VALUES (%s, %s)")
        values  = (name, task)
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()


def call_task(name, task):
    conn = connection_db("localhost", "root", "1111", "tasks")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ukoly")
    individual_tasks = cursor.fetchall()
    for i in individual_tasks:
        print(i)
    cursor.close()
    conn.close()


def show_tasks():
    conn  = connection_db("localhost", "root", "1111", "tasks")
    cursor = conn.cursor()
    cursor.execute("SELECT * from ukoly")
    individual_tasks = cursor.fetchall()
    if individual_tasks == "":
        return "Nemáte žádné úkoly."
    else:
        for i in individual_tasks:
            print(i)


def end():
    print("Konec programu.")


main_menu()