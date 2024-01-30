import os

source = "test_copy.txt"
destination = "/home/mate/Desktop/test.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print("Source was moved")
except FileNotFoundError:
    print(source)
