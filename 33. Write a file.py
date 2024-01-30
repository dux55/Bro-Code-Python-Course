text = "abc\ndef\n"

with open("test.txt", "w") as file:
    file.write(text)

with open("test.txt", "a") as file:
    file.write(text)
