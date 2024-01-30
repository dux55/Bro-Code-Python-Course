class Prey:
    def flee(self):
        print("Flee")

class Predator:
    def hunt(self):
        print("Hunting")

class Fish(Prey, Predator):
    pass


fish = Fish()
fish.flee()
fish.hunt()
