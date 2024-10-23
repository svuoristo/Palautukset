class Elevator:

    def __init__(self, ground_floor, top_floor):
        self.ground_floor = ground_floor
        self.top_floor = top_floor
        self.current_floor = self.ground_floor

    def go_up(self):
        self.current_floor = min(max(self.current_floor + 1, self.ground_floor), self.top_floor)
        print(f"Hissi on kerroksessa {self.current_floor}.")
        return

    def go_down(self):
        self.current_floor = min(max(self.current_floor - 1, self.ground_floor), self.top_floor)
        print(f"Hissi on kerroksessa {self.current_floor}.")
        return

    def go_to_floor(self, new_floor):
        while self.current_floor > new_floor and self.current_floor != self.ground_floor:
            self.go_down()
        while self.current_floor < new_floor and self.current_floor != self.top_floor:
            self.go_up()


class Building():

    def __init__(self, ground_floor, top_floor, elevator_amount):
        self.ground_floor = ground_floor
        self.top_floor = top_floor
        self.elevator_amount = elevator_amount
        self.elevators = []

        for i in range(elevator_amount):
            self.elevators.append(Elevator(ground_floor, top_floor))

    def use_elevator(self, elevator_number, target_floor):
        elevator = self.elevators[elevator_number - 1]
        elevator.go_to_floor(target_floor)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.ground_floor)

# t. 1
print("t. 1 Hissi toimii.")
elias_elevator = Elevator(-1, 5)
elias_elevator.go_to_floor(0)
elias_elevator.go_to_floor(6)
elias_elevator.go_to_floor(-1)

# t. 2
print("\nt. 2 Tervetuloa taloon!")
bilbo_building = Building(-2, 8, 4)
for i, _ in enumerate(bilbo_building.elevators):
    bilbo_building.use_elevator(i + 1, 2)

# t. 3
print("\nt. 3 Palohälytys!")
bilbo_building.fire_alarm()