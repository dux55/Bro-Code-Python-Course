class Car:
    make = None
    model = None
    year = None
    color = None

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

print(car_1.color)
car_1.drive()
