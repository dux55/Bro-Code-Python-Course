#List

food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]
print(food)
print(food[0])
print(food[4])

food[0] = "sushi"

for x in food:
    print(x)

food.append("ice cream")
food.remove("hotdog")
food.pop()
food.insert(0, "cake")
food.sort()
food.clear()
