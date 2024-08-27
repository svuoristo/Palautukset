import random

n = random.randint(1, 10)
arvaus = 0

while arvaus != n:
    arvaus = int(input("Arvaa luku jota ajattelen (1-10): "))
    if arvaus > n:
        print("Liian suuri arvaus.")
    elif arvaus < n:
        print("Liian pieni arvaus.")
    else:
        print("Oikein.")
