from string import Template
a = 1j
print(a.real, a.imag)
print(isinstance(a, complex))

print("Hello", "World", sep="//", end="\t")
print("Hello", "World 2", sep="//")

# C style formatting
print("Hello %s %d" % ("Trishan", 10))

# String Formatting
print("Hello {} {}".format("World", "2"))
print("Hello {1} {0}".format("World", "2", "100"))
print("My name is {name} and I am {age} years old".format(
    name="Trishan", age=17))

# Mixed Argument Formatting - Positiinal Arguments + Keyword Arguments
print("My name is {name} and I am {0} years old".format(
    17, name="Trishan"))

name = "Trishan"
age = 17
print(f"My name is {name} and I am {age} years old")

print(Template("My name is $name and I am $age years old").substitute(
    name=name, age=age))


# a = -91
# ~91
# 01011011
# 1 01011011
# 1 10100100
# 1 10100100
# 1 10100101
# 0 01011010
# 90
