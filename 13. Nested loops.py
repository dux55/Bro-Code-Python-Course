#Nested loops

rows = int(input("Rows: "))
columns = int(input("Columns: "))
symbol = input("Symbol: ")

print()
for i in range(rows):
    for j in range(columns):
        print(symbol, end = "")
    print()
