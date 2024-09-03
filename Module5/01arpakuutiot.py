import random

lkm = int(input("Anna arpakuutioiden määrä kokonaislukuna: "))
summa = 0

for noppa in range(lkm):
    n = random.randint(1, 6)
#    print("noppa: " + str(n))
    summa += n
#    print("summa: " + str(summa))

print(str(summa))