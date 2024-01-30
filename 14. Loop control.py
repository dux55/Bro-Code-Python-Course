while True:
    name = input("Name: ")
    if(name != ""):
        break

phone = "123-456-7890"
for i in phone:
    if(i == "-"):
        continue
    print(i, end="")

for i in range(1, 20+1):
    if i == 13:
        pass
    else:
        print(i)
