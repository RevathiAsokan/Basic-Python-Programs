""" To demonstrate function arguments
    default arguments: border = '-' (default value for border)"""

# Default arguments
def banner(message, border='-'):
    line = border * len(message)
    print("Message with default border")
    print(line)
    print(message)
    print(line)

# argument passing
def user_banner(message, border):
    line = border * len(message)
    print("Message with user defined border")
    print(line)
    print(message)
    print(line)

message = input("Enter a message to print: ")
border = input("Enter a border")

banner(message)
user_banner(message, border)

