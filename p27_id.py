""" Use of id - returns an unique and constant identifier
    for the life time of an object"""

a = 496
b = 1729

print("Value of a = {0}, ID of a = {1}".format(a, id(a)))
print("Value of b = {0}, ID of b = {1}".format(b, id(b)))

print("\nThe value of a is assigned to b")
b = a
print("Value of b = {0}, ID of b = {1}".format(b, id(b)))
if id(a) == id(b):
    print("id(a) == id(b)")
