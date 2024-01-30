from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("Car")
    def stop(self):
        print("Car")

class Motorcycle(Vehicle):
    def go(self):
        print("Motorcycle")
    def stop(self):
        print("Motorcycle")

#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go()
