# Import prepojenia na databázu
import db_connect as db


# Zoznam, do ktorého sa ukladajú úlohy
ukoly = [
    {
        "ukol": [],
        "popis": []
    }
    ]


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

    ukoly[0]["ukol"].append(nazev_ukolu)
    ukoly[0]["popis"].append(popis_ukolu)

    for item in range(len(ukoly[0]["ukol"])):
        print(f"Úkol \"{nazev_ukolu}\" byl přidán.")
       
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

    if ukoly[0]["ukol"] == []:
        print("\nNemáte žádné úkoly.")
    else:
        print("\nSeznam úkolů:")
        for item in range(len(ukoly[0]["ukol"])):
            print(f"{item+1}. {ukoly[0]["ukol"][item]} - {ukoly[0]["popis"][item]}")

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

    if ukoly[0]["ukol"] == []:
        print("\nNemáte žádné úkoly.")
        hlavni_menu()
    else:
        print("\nSeznam úkolů:")
        for item in range(len(ukoly[0]["ukol"])):
            print(f"{item+1}. {ukoly[0]["ukol"][item]} - {ukoly[0]["popis"][item]}")

        while True:
            try:
                odstraneny_ukol = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
            except ValueError:
                continue
            if odstraneny_ukol <= 0:
                print("Nesprávny vstup.")
                continue
            break
        x = ukoly[0]["ukol"][odstraneny_ukol - 1]
        del ukoly[0]["ukol"][odstraneny_ukol - 1]
        del ukoly[0]["popis"][odstraneny_ukol - 1]
        print(f"Úkol \"{x}\" byl odstraněn.")

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
hlavni_menu()