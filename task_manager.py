ukoly = [
    {
        "ukol": [],
        "popis": []
    }
    ]

def pridat_ukol():
    while True:
        x = input("Zadejte název úkolu: ")
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
    for item in range(len(ukoly[0]["ukol"])):
        print(ukoly[0]["ukol"][item])
        print(ukoly[0]["popis"][item])
    hlavni_menu()

def odstranit_ukol():
    print("Something")

def konec_programu():
    print("Konec")

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