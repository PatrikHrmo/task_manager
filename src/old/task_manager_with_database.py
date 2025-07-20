# Import prepojenia na databázu
from old.db_connect import pripojeni_db as db
conn = db("localhost", "root", "1111", "ukoly")

# Vytvorenie databazy ukoly, pokial neexistuje, a tabulky ukoly.
def inicializace_db():

    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ukoly")
    cursor.execute("USE ukoly")
    cursor.execute("""CREATE TABLE IF NOT EXISTS ukoly (
	    id INT auto_increment PRIMARY KEY,
        nazev VARCHAR(255) NOT NULL,
        popis VARCHAR(255) NOT NULL,
        stav ENUM("nezahájeno","probíhá","hotovo") DEFAULT "nezahájeno",
        datum_vytvoreni DATETIME DEFAULT CURRENT_TIMESTAMP)
    """)
    cursor.close()


# Hlavné menu, ktoré zobrazí 4 operácie, ktorým prináležia 4 funkcie. Pri zadaní nesprávnej hodnoty program vráti požiadavku alebo upozorní na chybu.
def hlavni_menu():

    print("\nSprávce úkolů - Hlavní menu")
    print("1. Přidat nový úkol")
    print("2. Zobrazit všechny úkoly")
    print("3. Odstranit úkol")
    print("4. Konec programu")

    while True:
        try:
            moznost = int(input("Vyberte možnost (1-4): "))
        except ValueError:
            continue
        if moznost > 0 and moznost <= 4:
            break
    if moznost == 1:
        return pridat_ukol()
    elif moznost == 2:
        return zobrazit_ukoly()
    elif moznost == 3:
        return odstranit_ukol()
    elif moznost == 4:
        return konec_programu()


# Funkcia pridá názov a popis úlohy. Pri prázdnej hodnote program zopakuje požiadavku. Po pridaní úlohy sa otvorí hlavné menu.
def pridat_ukol():

    while True:
        nazev_ukolu = input("\nZadejte název úkolu: ")
        if nazev_ukolu == "":
            print("Prázdný vstup.")
            continue
        break
    while True:
        popis_ukolu = input("Zadejte popis úkolu: ")
        if popis_ukolu == "":
            print("Prázdný vstup.")
            continue
        break
    
    cursor = conn.cursor()

    sql = ("INSERT INTO ukoly (nazev, popis) VALUES (%s, %s)")
    values  = (nazev_ukolu, popis_ukolu)
    cursor.execute(sql, values)
    conn.commit()

    cursor.execute("SELECT * FROM ukoly")
    jednotlive_ukoly = cursor.fetchall()

    for i in jednotlive_ukoly:
        print(i)

    cursor.close()
       
    print("\nSprávce úkolů - Hlavní menu")
    print("1. Přidat nový úkol")
    print("2. Zobrazit všechny úkoly")
    print("3. Odstranit úkol")
    print("4. Konec programu")

    while True:
        try:
            moznost = int(input("Vyberte možnost (1-4): "))
        except ValueError:
            continue
        if moznost > 0 and moznost <= 4:
            break
    if moznost == 1:
        return pridat_ukol()
    elif moznost == 2:
        return zobrazit_ukoly()
    elif moznost == 3:
        return odstranit_ukol()
    elif moznost == 4:
        return konec_programu()


# Zobrazí všetky úlohy. Pokiaľ žiadna úloha neexistuje, zobrazí sa správa o neexistujúcich úlohách. Po skončení sa zobrazí hlavné menu.
def zobrazit_ukoly():

    cursor = conn.cursor()

    cursor.execute("SELECT * from ukoly")
    jednotlive_ukoly = cursor.fetchall()

    if not jednotlive_ukoly:
        print("\nNemáte žádné úkoly.")
    else:
        for i in jednotlive_ukoly:
            print(i)
    
    conn.commit()
    cursor.close()

    print("\nSprávce úkolů - Hlavní menu")
    print("1. Přidat nový úkol")
    print("2. Zobrazit všechny úkoly")
    print("3. Odstranit úkol")
    print("4. Konec programu")

    while True:
        try:
            moznost = int(input("Vyberte možnost (1-4): "))
        except ValueError:
            continue
        if moznost > 0 and moznost <= 4:
            break
    if moznost == 1:
        return pridat_ukol()
    elif moznost == 2:
        return zobrazit_ukoly()
    elif moznost == 3:
        return odstranit_ukol()
    elif moznost == 4:
        return konec_programu()


# Pokiaľ existujú úlohy, program ich zobrazí a uživateľ ich bude môcť vymazať. Ak neexistujú žiadne úlohy, program zobrazí správu o neexistujúcich úlohách. Po skončení sa zobrazí hlavné menu.
def odstranit_ukol():

    cursor = conn.cursor()

    cursor.execute("SELECT * from ukoly")
    jednotlive_ukoly = cursor.fetchall()

    if not jednotlive_ukoly:
        print("\nNemáte žádné úkoly.")
    else:
        for i in jednotlive_ukoly:
            print(i)

    while True:
        try:
            odstraneny_ukol = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
        except ValueError:
            continue
        if odstraneny_ukol <= 0:
            print("Nesprávny vstup.")
            continue
        break

    sql = "DELETE FROM ukoly WHERE id = %s"
    values = (odstraneny_ukol,)
    cursor.execute(sql, values)

    conn.commit()
    cursor.close()

    print(f"Úkol \"{odstraneny_ukol}\" byl odstraněn.")

    print("\nSprávce úkolů - Hlavní menu")
    print("1. Přidat nový úkol")
    print("2. Zobrazit všechny úkoly")
    print("3. Odstranit úkol")
    print("4. Konec programu")

    while True:
        try:
            moznost = int(input("Vyberte možnost (1-4): "))
        except ValueError:
            continue
        if moznost > 0 and moznost <= 4:
            break
    if moznost == 1:
        return pridat_ukol()
    elif moznost == 2:
        return zobrazit_ukoly()
    elif moznost == 3:
        return odstranit_ukol()
    elif moznost == 4:
        return konec_programu()


# Ukončenie programu vypísaním hlásenia o skončení programu.
def konec_programu():
    print("\nKonec programu.")


# Spustenie programu
inicializace_db()
hlavni_menu()


# Zatvorenie pripojenia na databázu
conn.close()