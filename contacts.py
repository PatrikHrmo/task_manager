contacts = [
    {
        "meno": "Patrik",
        "priezvisko": "Hrmo",
        "vek": "32"
    },
    {
        "meno": "Lenka",
        "priezvisko": "Blahova",
        "vek": "27"
    }
]

print(contacts[0])

print(contacts[0]["meno"])

meno = "Anicka"
priezvisko = "Ahahash"
vek = "33"

contact = {
    "meno": meno,
    "priezvisko": priezvisko,
    "vek": vek
}

contacts.append(contact)
print(contacts)