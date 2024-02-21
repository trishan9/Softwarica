from functools import reduce

print("Trishan\n"*100)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[2: 7])


for i in range(1, 21):
    print(f"{i} = Trishan")

for i, char in enumerate("Trishan"):
    print(i, char)


user_input = int(input("Enter the number for multiplication table: "))

for n in range(1, 11):
    print(f"{user_input} * {n} = {user_input * n}")

for n in range(10, 0, -1):
    print(f"{user_input} * {n} = {user_input * n}")


numbers = [1, 2, 3, 4, 5]

sum_of_numbers = reduce(lambda a, b: a + b, numbers)
product_of_numbers = reduce(lambda a, b: a * b, numbers)
odd_numbers = [n for n in numbers if not (n % 2 == 0)]
even_numbers = [n for n in numbers if n % 2 == 0]

print(sum_of_numbers)
print(product_of_numbers)
print(odd_numbers)
print(even_numbers)

data = [1, 2, 2.5, "trishan", [1, 2], {1, 2}, {1: 2, 2: 3}, (1, 5)]
data_types = [type(a) for a in data]
print(data_types)
