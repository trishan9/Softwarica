a = "Python Hello"
print(a.capitalize())
print(a.title())

print(a.rjust(len(a) + 6, "*"))
print(a.ljust(len(a) + 6, "*"))

b = "Python"
c = "Pytho"
print(b.center(13, "*"))
print(c.center(12, "*"))

''' 
Center Rule
n refers to width - length of string 
Even(length) Formula - Left: n+1/2
Odd(length) Formula - Left: n-1/2
'''

a = "Softwarica"
b = a.center(16, "*")
print(b[1:])

print(a.zfill(len(a) + 3))
b = "+Python"
print(b.zfill(len(b) + 3))

name = "PythonP"
print(name.upper())
print(name.lower())
print(name.swapcase())
print(a.istitle())

print(name.find('o'))
print(name.rfind('o'))  # -1
print(name.index('P'))  # error
print(name.rindex('P'))

print(name.count("P"))

print(name.isupper())
print(name.islower())

print(name.isdigit())
a = "000"
print(a.isdigit())

print(name.isalnum())
print(name.isalpha())

print(a.isspace())
b = "    "
print(b.isspace())
print(a.isidentifier())
print(a.isprintable())
