import random

def heitanoppaa(tahkot):
    saatu = random.randint(1, tahkot)
    return saatu

tahko = int(input("Anna nopan tahkojen määrä kokonaislukuna: "))
heitto = heitanoppaa(tahko)

while heitto != tahko:
    heitto = heitanoppaa(tahko)
    print(str(heitto))