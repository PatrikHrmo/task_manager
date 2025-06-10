seznam_ukolu = [
    {
        "ukol": [],
        "popis": []
    }
    ]

def pridat_ukol():
    while True:
        x = input("\nZadejte názov úkolu: ")
        y = input("Popis úkolu: ")
        if x != "" and y != "":
            break
    seznam_ukolu[0]["ukol"].append(x)
    seznam_ukolu[0]["popis"].append(y)
   
    for item in range(len(seznam_ukolu[0]["ukol"])):
        print(f"Úkol {item+1} byl přidán.\n")
       
    hlavni_menu()

def zobrazit_ukoly():
    for item in range(len(seznam_ukolu[0]["ukol"])):
        print(seznam_ukolu[0]["ukol"][item])
        print(seznam_ukolu[0]["popis"][item])
    hlavni_menu()

def odstranit_ukol():
    print("Something")

def konec_programu():
    print("Konec")

def hlavni_menu():
    print("""Správce úkolú - hlavní menu
    1. přidat nový úkol
    2. Zobrazit všechny úkoly
    3. Odstranit úkol
    4. Konec programu\n""")
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