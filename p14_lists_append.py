""" To demonstrate append() in Lists"""

fruits = ["apple", "banana"]

for i in fruits:
    response = input("Would like to add a fruit? ")
    if response == "yes" and len(fruits) < 5:
        new_fruit = input("Enter name of a fruit : ")
        fruits.append(new_fruit)
        print("{0} added to fruits".format(new_fruit))
    elif len(fruits) >= 5:
        print("Maximum limit exceeded")
        break
    else:
        print("The fruits in the list are : {0}".format(fruits))
        break
