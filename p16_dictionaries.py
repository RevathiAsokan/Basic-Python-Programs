""" To demonstrate dictionaries
    create an empty dictionary
    print a dictionary
    add and print values"""


e = {}  # empty dictionary
print(e, "is an empty dictionary")

d = {'alice': '984-558-9256', 'bob': '896-458-1236'}
print("\nThe values in d = {}".format(d))

print("\nAdd a value to d")
name = input("Enter name: ")
d[name] = input("contact no")
print("Added {}".format(d[name]))
print("Final Dictionary = {}".format(d))

print("\nPrint a value of d")
name = input("Enter name: ")
print("Contact no. of ", name, "is", d[name])

