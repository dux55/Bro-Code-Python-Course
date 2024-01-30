def hello(**kwargs):
    #print("Hello, "+kwargs['first']+" "+kwargs['last'])
    print("Hello,", end=" ")
    for x,y in kwargs.items():
        print(y, end=" ")
    print()

hello(first="Dux", mid="King", last="5")
