import random
from tabulate import tabulate

class Car:
    def __init__(self, license_number, top_speed, speed = 0, travel_ditance = 0):
        self.license_number = license_number
        self.top_speed = top_speed
        self.speed = speed
        self.travel_distance = travel_ditance

    def accelerate(self, acceleration):
        self.speed = min(self.top_speed, max(0, self.speed + acceleration))
        return

    def progress(self, hours):
        self.travel_distance += hours * self.speed

    def __str__(self):
        r = self.license_number
        h = str(self.top_speed)
        n = str(self.speed)
        m = str(self.travel_distance)
        return 'Auto(rekkari: ' + r + ' huippunopeus: ' + h  + ' km/h, nopeus: ' + n + ' km/h, matka: ' + m + ' km)'

class Race:
    def __init__(self, name, length, cars):
        self.name = name
        self.length = length
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.progress(1)

    def print_status(self):
        cars = sorted(self.cars, key=lambda car: car.travel_distance, reverse=True)
        car_info = []
        for car in cars:
            car_info.append([cars.index(car) +  1, car.license_number, car.top_speed, car.speed, car.travel_distance])
        print(tabulate(car_info,
                         headers=['sija', 'rekisterinumero', 'huippunopeus (km/h)', 'nopeus (km/h)','kuljettu_matka (km)'],
                         tablefmt="grid"))
    def race_over(self):
        for car in self.cars:
            if car.travel_distance >= self.length:
                return True
        return False

boyz_cars = []
for num in range(10):
    license_plate = f'ABC-{num + 1}'
    top_speed = random.randint(100, 200)
    boyz_cars.append(Car(license_plate, top_speed))

big_romu_race = Race("Suuri romuralli", 8000, boyz_cars)

hours = 0
while not big_romu_race.race_over():
    big_romu_race.hour_passes()
    hours += 1

    if hours % 10 == 0:
        print(f"\nKisaa on ajettu {hours} tuntia.")
        big_romu_race.print_status()

print(f"\nKisa päättyi! Sitä ajettiin {hours} tuntia. Onnea voittajalle.")
big_romu_race.print_status()
