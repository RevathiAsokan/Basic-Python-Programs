""" To demonstrate break statement
    Accept only even number and quit when user enters odd number"""

while True:
    num = input("Enter a even number: ")
    if int(num) % 2 != 0:
        print("Program ends! You have entered a odd number")
        break
