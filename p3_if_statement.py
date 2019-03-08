""" To demonstrate if statement
    find if the person is eligible to vote or not"""

age = int(input("Enter the age of the person: "))
citizenship = input("Whether citizen of India, yes or no: ")

if citizenship == "yes" and age >= 18:
    print("Eligible to vote".format(age))
else:
    print("Not eligible to vote".format(age))
