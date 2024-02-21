a = "softwarica"

print(a.upper())


a = "@@PYTHON"

print(a.isupper())


a = "@@PYTHON"

print("a".isupper())


a = "capital"

print("A".isupper())


a = "capital"

print("a")


a = "capital"

# print(a.capitalize("c"))


a = "      capital"

print(a.isalnum())


a = "capital"

print(a.isalnum())


a = "1Capital"

print(a.zfill(9))


a = "+Capital"

print(a.zfill(9))


a = "-Capital"

print(a.zfill(9))


a = "$Capital"

print(a.zfill(9))


a = "$Capital"

# print(a.zfill(9, "*"))


a = "$Capital"

# print(a.center(9, "**"))


a = "$Capital"

print(a.center(9, "*"))


a = "+Capital"

print(a.center(9, "*"))


a = "+Capital9"

print(a.count("9"))


a = "+Cap9ital9"

print(a.find("9"))


a = "+Cap9ital9"

print(a.rfind("9"))


a = "+Cap9ital9"

print(a.find("A"))


a = "+Cap9ital9"

# print(a.index("A"))


a = "Cap9"

print(a.isdigit())


a = "pythON9"

print(a.swapcase())


a = "\t"

print(a.isspace())


a = "\t"

print(a.isprintable())


a = "123abc"

print(a.isalpha())


a = "123abc"

print(a.rjust(11, "#"))


a = "123abc"

print(a.ljust(11, "#"))


a = "123abc"

print(a.ljust(6, "#"))


# for="123abc"

# print(for.ljust(6,"#"))


a = "123abc"

print(a.replace('w', "1"))


a = "123abc"

b = a.count("c")

print(b)


a = "123abc"

b = a.maketrans("123", "abc")

print(a.translate(b))


a = "123abc"

b = a.maketrans("123", "abc")

print(b)


a = "123abc"

b = a.maketrans("A", "a")

print(b)


a = "123abc"

# b = a.maketrans("ab", "A")

print(b)


a = "123abc"

b = a.startswith("123")

print(a)


a = "123abc"

b = a.endswith("abc")

print(a)


a = "123abc"

b = a.endswith("c")

print(a)


a = "123abc"

print(a.replace('ab', "1"))
