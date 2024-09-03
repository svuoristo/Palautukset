import random

lkm = int(input("Anna arpakuutioiden määrä kokonaislukuna: "))
summa = 0

for noppa in range(1, lkm + 1):
    summa = summa + random.randint(1, 6)

print(str(summa))