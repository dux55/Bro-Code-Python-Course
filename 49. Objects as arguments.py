class Car:
    color = None

def change_color(car, color):
    car.color = color

car_1 = Car()
print(car_1.color)
change_color(car_1, "Green")
print(car_1.color)
