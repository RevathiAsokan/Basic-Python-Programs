""" To demonstrate while statement explicit
    print tables of any number """

num = int(input("Enter a number: "))
i = 1

while i <= 10:  # Explicit is better than implicit
    print(num*i)
    i += 1
