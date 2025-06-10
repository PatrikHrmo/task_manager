ukoly = [
    {
        "ukol": [],
        "popis": []
    }
    ]


def pridat_ukol():

    while True:
        x = input("\nZadejte název úkolu: ")
        if x == "":
            print("Prázdný vstup.")
            continue
        break
    while True:
        y = input("Zadejte popis úkolu: ")
        if y == "":
            print("Prázdný vstup.")
            continue
        break

    ukoly[0]["ukol"].append(x)
    ukoly[0]["popis"].append(y)

    for item in range(len(ukoly[0]["ukol"])):
        print(f"Úkol \"{x}\" byl přidán.")
       
    hlavni_menu()


def zobrazit_ukoly():

    if ukoly[0]["ukol"] == []:
        print("\nNemáte žádné úkoly.")
    else:
        print("\nSeznam úkolů:")
        for item in range(len(ukoly[0]["ukol"])):
            print(f"{item+1}. {ukoly[0]["ukol"][item]} - {ukoly[0]["popis"][item]}")

    hlavni_menu()


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
        z = ukoly[0]["ukol"][odstraneny_ukol - 1]
        del ukoly[0]["ukol"][odstraneny_ukol - 1]
        del ukoly[0]["popis"][odstraneny_ukol - 1]
        print(f"Úkol \"{z}\" byl odstraněn.")

        hlavni_menu()


def konec_programu():
    print("\nKonec programu.")


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

hlavni_menu()