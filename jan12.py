a = [1, 2, 3, 4]
a.append(5)
a.extend([1, 2])
a.insert(0, 100)
a.pop(0)
a.remove(3)
a[0] = 1000
del a[len(a) - 1]
print(a)

a = [1, 2, 3, 4]
b = a.copy()
b.append(5)
print(a)

a = [1, 2, 3, 4]
b = list(a)
b.insert(2, 100)
a = tuple(b)
print(a)

a = {1, 2, 3, 4}
b = {3, 4, 5}
a.add(5)
a.update(b)
a.remove(5)
a.discard(900)
a.pop()  # -> removes first elemen
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a)

a = {"a": 1, "b": 2}
a.setdefault("a", 3)
a.setdefault("c", 100)
print(a)

b = a.get(
    "d", "Hello"
)  # -> doesn't give error, instead retutns None but if Second Arg is passed then Second Arg is returned
print(b)
