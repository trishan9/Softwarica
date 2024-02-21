from functools import reduce
import random
import math
import datetime
from datetime import timedelta

lst = [1, 2, 3, 4, 5]
list2 = map(lambda x: x**2, lst)
print(list(list2))

list2 = filter(lambda x: x % 2 == 0, lst)
print(list(list2))

list2 = reduce(lambda x, y: x + y, lst, 0)
print(list2)


def greet(name):
    print(f"Hello {name}")


if __name__ == "__main__":
    greet("Trishan")

print(random.random())  # Returns float, includes 0 excludes 1
print(random.randrange(1, 8, 2))  # Returns Integer and includes 1-7 with step2
print(random.randint(1, 8))  # Returns Integer and includes 1-8
print(random.uniform(1, 8))  # Returns Float and includes 1-7

print(math.floor(1.8))
print(math.ceil(1.8))
print(math.ceil(1.0))
print(math.sqrt(4))
print(math.pow(2, 3))
print(math.fabs(18))
print(math.fabs(-18))

today = datetime.datetime.now()
tomorrow = today + timedelta(days=365)
print(tomorrow)
print(today.strftime("%Y/%m/%d"))
