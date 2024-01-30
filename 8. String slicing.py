#By index
name = "Dux5"
first_name = name[:3]
last_name = name[3:]
print(first_name)
print(last_name)
print(name[::2])

reversed_name = name[::-1]
print(reversed_name)

print()

#By slice object
website1 = "https://google.com"
website2 = "https://wikipedia.com"
slice = slice(8, -4)
print(website1[slice])
print(website2[slice])
