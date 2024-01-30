#Class of an object is less important than the members
#Class type is not checked if minimum members are present

class Duck:
    def walk(self):
        print("Duck is walking")
    def talk(self):
        print("Duck is talking")

class Chicken:
    def walk(self):
        print("Chicken is walking")
    def talk(self):
        print("Chicken is talking")

class Person():
    def catch(self, duck):
        duck.walk()
        duck.talk()


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)
