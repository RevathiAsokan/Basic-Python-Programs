""" To demonstrate while statement (implicit)
    print reverse series of any number while statement """

num = int(input("Enter a number: "))

print("The reverse series of {0} is \n".format(num))

while num:
    print(num)
    num -= 1
