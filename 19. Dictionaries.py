capitals = {"USA":"Washington DC",
            "India":"New Dehli",
            "China":"Peking",
            "Russia":"Moscow"
            }

print(capitals["Russia"])
print(capitals.get("Germany"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
print(capitals)

capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Las Vegas"})
capitals.pop("China")

for x, y in capitals.items():
    print(f"{x}, {y}")

capitals.clear()
