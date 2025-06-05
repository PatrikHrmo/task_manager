meno = input("Napíš svoje meno: ")
stastie = input ("Vyber si citát na dnešný deň. Napíš a, b alebo c: ")

stastie = stastie.lower()

if stastie == "a":
    print(f"Milovaná {meno}, si najlepšia na svete!")
elif stastie == "b":
    print(f"Milovaná {meno}, máš skvelé vlasy!")
else:
    print(f"Milovaná {meno}, máš krásne srdieško.")

print("Ďakujem za pozornosť a milujem ťa. :D")