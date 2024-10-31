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

class ElectricCar(Car):
    def __init__(self, license_number, top_speed,  battery_capacity, speed = 0, travel_distance = 0):
        self.battery_capacity = battery_capacity
        Car.__init__(self, license_number, top_speed, speed, travel_distance)

class CombustionEngineCar(Car):
    def __init__(self, license_number, top_speed, tank_capacity, speed = 0, travel_distance = 0):
        self.tank_capacity = tank_capacity
        Car.__init__(self, license_number, top_speed, speed, travel_distance)

blue_car = ElectricCar('ABC-15', 180, 52.5)
red_car = CombustionEngineCar('ACD-123', 165, 32.3)

blue_car.accelerate(140)
red_car.accelerate(140)
blue_car.progress(3)
red_car.progress(3)

print(blue_car.__str__())
print(red_car.__str__())