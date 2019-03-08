""" To demonstrate lists
    Lists are mutable sequences of objects"""

fruits = ["apple", "orange", "papaya", "mango", "banana"]
num = int(input("Enter your choice (1-5) to find and replace a fruit : "))
choice = num - 1
size = len(fruits)

if num != 0 and num <= size:
    print("You choose no. {0} with {1} fruit".format(num, fruits[choice]))
    fruits[num] = input("Enter a fruit to replace:")
    print("Fruits = ", fruits)
else:
    print("Error: Enter numbers between 1 and 5")

print("\nNote: Data type of the variable fruits is {0}".format(type(fruits)))

