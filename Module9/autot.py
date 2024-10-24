import random
from tabulate import tabulate

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdyta(self, muutos):
        self.nopeus = min(self.huippunopeus, max(0, self.nopeus + muutos))
        return

    def kulje(self, tunnit):
        self.kuljettu_matka += tunnit * self.nopeus

    def __str__(self):
        r = self.rekisteritunnus
        h = str(self.huippunopeus)
        n = str(self.nopeus)
        m = str(self.kuljettu_matka)
        return 'Auto(rekkari: ' + r + ' huippunopeus: ' + h  + ' km/h, nopeus: ' + n + ' km/h, matka: ' + m + ' km)'


# t. 1
print("t. 1")
punainen_auto = Auto("ABC-123", 142)
print(f"Auton {punainen_auto.rekisteritunnus:s} kulkee nopeimmillaan {punainen_auto.huippunopeus:d} km/h. "
      f"Nyt sen nopeus on {punainen_auto.nopeus:d} km/h "
      f"ja sillä on kuljettu {punainen_auto.kuljettu_matka:d} km.")

# t. 2
print("t. 2")
punainen_auto.kiihdyta(30)
punainen_auto.kiihdyta(70)
punainen_auto.kiihdyta(50)
print(punainen_auto.nopeus)
punainen_auto.kiihdyta(-200)
print(punainen_auto.nopeus)

# t. 3
print("t. 3")
punainen_auto.kiihdyta(100)
punainen_auto.kulje(20)
print(punainen_auto.kuljettu_matka)
punainen_auto.kiihdyta(-40)
punainen_auto.kulje(1.5)
print(punainen_auto.kuljettu_matka)

# t. 4
print("t. 4")
autot = []
for num in range(10):
    rekkari = f'ABC-{num + 1}'
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekkari, huippunopeus))

kisa_ohi = False
while not kisa_ohi:
    for auto in autot:
        auto.kiihdyta(random.randint(-10, 15))
        auto.kulje(1)
        if auto.kuljettu_matka >= 10000:
            kisa_ohi = True
            break

auto_info = []
for auto in autot:
    auto_info.append([auto.rekisteritunnus, auto.huippunopeus, auto.nopeus, auto.kuljettu_matka])

print(tabulate(auto_info, headers=['rekkari', 'huippunopeus (km/h)', 'nopeus (km/h)', 'kuljettu_matka (km)'], tablefmt="grid"))