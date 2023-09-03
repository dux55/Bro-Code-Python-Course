#Set

utensils = {"fork", "spoon", "knife", "knife"}

utensils.add("napkin")
utensils.remove("spoon")
print(utensils)

dishes = {"bowl", "plate", "cup", "knife"}

print()

print(utensils.difference(dishes))
print(dishes.difference(utensils))
print(utensils.intersection(dishes))

print()

dinner_table = utensils.union(dishes)
print(dinner_table)

utensils.update(dishes)
print(utensils)
