try:
    a = int(input("Enter Number: "))
    b = int(input("Enter Number: "))
    print(a/b)
except ZeroDivisionError as e:
    print("You tried to divide by zero")
    print(e.args)
except ValueError as e:
    print("Bad Input")
    print(e.args)
except BaseException as e:
    print(e.args)
print("A")
