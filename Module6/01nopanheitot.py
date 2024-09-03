import random

def heitanoppaa():
    heitto = random.randint(1, 6)
    return heitto

heitto = 0

while heitto != 6:
    heitto = heitanoppaa()
    print(str(heitto))