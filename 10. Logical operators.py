#Logical operators

temperature = int(input("Temperature: "))

if not(0 <= temperature and temperature <= 30):
    print("Bad")
elif not(temperature < 0 or temperature > 30):
    print("Good")
