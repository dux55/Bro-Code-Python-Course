class Car:
    make = None
    model = None
    year = None
    color = None
    wheels = 4

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def drive(self):
        print(f"Drive ({self.model})")
    def stop(self):
        print("Stop")

car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_1.wheels = 2

print(Car.wheels)
Car.wheels = 1
