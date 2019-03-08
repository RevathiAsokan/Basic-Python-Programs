""" To demonstrate functions
    - Square of a number
    - Check odd or even"""


def square(y):
    return y * y


x = int(input("Enter a number to find its square: "))
s = square(x)
print("Square of ", x, "is ", s)


def check(num):
    if num % 2 == 0:
        print(num, "is an even number")
    else:
        print(num, "is an odd number")


number = int(input("Enter a number to check it is even or odd: "))
check(number)
