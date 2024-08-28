import random
# pi ≈ 4n/N

n_kok = int(input("Anna arvottavien pisteiden määrä kokonaislukuna: "))
n_sis = 0
nykyinen = 0

while nykyinen < n_kok:

    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    if x**2 + y**2 < 1.0:
        n_sis += 1
    nykyinen += 1

print((4*n_sis)/n_kok)