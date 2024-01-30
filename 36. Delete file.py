import os

path = "test.txt"

try:
    os.remove(path)
except FileNotFoundError:
    print("That file was not found")
