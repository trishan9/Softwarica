def greet():
    '''This function prints hello world'''
    print("Hello World")


print(greet.__doc__)

# Arithmetic Operator
a = 5
a1 = "5"
b = 6

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
print(a // b)

# Assignment Operators
b += 1
b -= 1
b *= 1
b /= 1
b **= 1
b //= 1

# Comparison Operators
print(a == a1)
print(a != a1)
print(a < b)
print(a > b)
print(a >= b)
print(a <= b)

# Logical Operators
print(2 < 3 and 3 > 4)
print(2 < 3 and 3)  # True and Expression = Expression
print(2 > 3 and 3)  # False and Expression = False

print(2 < 3 or 3 > 4)
print(2 < 3 or 3)  # True or Expression = True
print(2 > 3 or 3)  # False or Expression = Expression

# Identity Operator
a = 10
a1 = 10
print(a is a1)
print(a is not a1)

# Membership Operator
a = "Python"
print("n" in a)
print("N" not in a)


# Bitwise Operator
a = 24
b = 20
print(bin(a))
print(bin(b))
print(a & b)  # 10000 = 16
print(a | b)  # 11100 = 28
print

# Bitwise NOT
# sign exponent mantisa
# 0 - Pos
# 1 - Neg
# 0 - 1001
# 1 - 0110 - 2's Complement, but first 1 complement
# 1's Complement flip all bit except sign bit
# 2's Complement add 1
# print(a  b)

print(~8)
print(bin(8))  # 1000
# Pos Sign Bit + Truth Table - 1 0111 - Negative Number Skips this Process and does it ast last
# 1's Complement - 1 1000
# 2's Complement - 1 1000 + 1 = 1001
# Final Binary = 1 1001 -> -9

print(f"{0.1:.20f}")
print(f"{0.2:.20f}")
print(f"{0.3:.20f}")
print(f"{0.1 + 0.2:.20f}")
