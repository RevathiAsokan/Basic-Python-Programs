""" Demonstrate variable scoping"""

count = 0

def show_count():
    print("count = ", count)


def set_count(c):
    print("New local binding of count")
    count = c  # new, local binding of "count"
    show_count()


def set_new_count(c):
    print("Using global keyword")
    global count
    count = c
    show_count()

print("Passing the value of 5 to set_count()")
set_count(5)  # Passed the value as 5, returns o
print("\nPassing the value of 10 to set_new_count()")
set_new_count(10)  # Passed the value as 10, returns 10
