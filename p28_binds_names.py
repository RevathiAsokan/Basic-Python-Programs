""" To demonstrate python binds
    only by names, never by value """

r = [2, 4, 6]
print("The value of r = ", r)
s = r
print("The value of s = ", s)

print("Assigning 17 to s[1]")
s[1] = 17
print("The value of r = ", r)
print("The value of s = ", s)


