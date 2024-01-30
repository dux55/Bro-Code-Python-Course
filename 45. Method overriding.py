class Animal:
    def eat(self):
        print("Eating")

class Rabbit(Animal):
    def eat(self):
        print("Rabbit is eating")

rabbit = Rabbit()
rabbit.eat()
