def get_age():
    age = int(input("Enter Your Age:"))
    if age < 0:
        raise ValueError("Age can't be negative")


def d():
    c()


def c():
    b()


def b():
    a()


def a():
    get_age()


try:
    d()
except ValueError as e:
    print(e.args[0])
