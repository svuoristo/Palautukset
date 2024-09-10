name = input("Anna nimi: ")
names = set()
while name != "":
    if name in names:
        print("Aiemmin syötetty nimi.")
    else:
        print("Uusi nimi.")
    names.add(name)
    name = input("Anna nimi: ")


print("Nimet ovat: ")
for n in names:
    print(n)