try:
    with open("test.tx") as file:
        print(file.read())
    print(file.closed)
except FileNotFoundError:
    print("That file was not found :(")
