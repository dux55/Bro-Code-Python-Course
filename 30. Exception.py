try:
    numerator = int(input())
    denominator = int(input())
    res = numerator/denominator
except ZeroDivisionError:
    print("You fool, what have you done?!")
except ValueError:
    print("What?")
except Exception as E:
    print(E)
else:
    print(res)
finally:
    print("Done!")
