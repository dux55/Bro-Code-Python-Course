#Random
import random

x = random.randint(1, 6)
y = random.random()

my_list =  ["rock", "paper", "scissors"]
z = random.choice(my_list)

print(x)
print(y)
print(z)

perm = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(perm)
print(perm)
