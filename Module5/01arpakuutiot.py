import random

lkm = int(input("Anna arpakuutioiden määrä kokonaislukuna: "))
summa = 0

for noppa in range(lkm):
    n = random.randint(1, 6)
    summa += n

print(str(summa))