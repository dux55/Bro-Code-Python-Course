class Car:
    def turn_on(self):
        print("Turned on")
        return self
    def drive(self):
        print("Drive")
        return self
    def brake(self):
        print("Braking")
        return self
    def turn_off(self):
        print("Turned off")
        return self


car = Car()
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()
