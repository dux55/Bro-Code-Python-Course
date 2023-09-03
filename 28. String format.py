#str.format()

animal = "cow"
item = "moon"

print("The {} jumped over the {}".format(animal, item))
print("The {1} jumped over the {0}".format(item, animal))

text = "The {} jumped over the {}"
print(text.format(animal, item))

name = "Dux"
print("Hello, my name is {:10} nice to meet you!".format(name))
print("Hello, my name is {:<10} nice to meet you!".format(name))
print("Hello, my name is {:>10} nice to meet you!".format(name))
print("Hello, my name is {:^10} nice to meet you!".format(name))

pi = 3.14159
print("The number pi is {:.2f}".format(pi))

num = 32
print("The number {} is {:b}".format(num, num))
print("The number {} is {:o}".format(num, num))
print("The number {} is {:X}".format(num, num))
print("The number {} is {:E}".format(num, num))
