luku = int(input("Anna nollaa suurempi koknaisluku: "))
alkuluku = True

if luku <= 0:
    print("Luku ei ole alkuluku.")

else:
    for jakaja in range(2, luku):
        if luku % jakaja == 0:
            alkuluku = False
    if alkuluku:
        print("Luku on alkuluku.")
    else:
        print("Luku ei ole alkuluku.")



