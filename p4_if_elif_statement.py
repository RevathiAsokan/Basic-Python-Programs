""" To demonstrate if elif statement
    find whether a number lies in a range or not """

start = int(input("Enter the value of start of range: "))
end = int(input("Enter the value of end of range: "))
num = int(input("Enter the number to find in range: "))

if num > end:
    print(num, "greater than ", end)
elif num < start:
    print(num, "less than ", start)
else:
    print(num, "is in range ", start, " - ", end)
