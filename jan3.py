def add(a, b, c):
    print(a + b + c)


add(1, 2, 3)


def add(a, b, c):
    print(a + b + c)


add(a=1, b=2, c=3)


def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


print(add(1, 2, 3, 4, 5))


def add(sum=0, *args):
    for arg in args:
        sum += arg
    return sum


print(add(5, 1, 2, 3, 4, 5))


def area(*args, **kwargs):
    area_of_rectangle = kwargs['length'] * kwargs['breadth']
    print(args, area_of_rectangle)


area(length=10, breadth=5)
