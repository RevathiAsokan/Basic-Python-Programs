""" Default argument values are evaluated when def is evaluated.
    They can be modified like any other object"""

# Default argument values
""" The empty list created for the default arguments
    is created once, when the statement is executed,
    the list is added with spam to it by default
    when add_spam is called without any argument
    spam is added to the empty list created"""

def add_spam(menu=[]):
    menu.append("spam")
    return menu

breakfast = ['bacon', 'eggs']
add_spam(breakfast)
print("The value of breakfast = ", breakfast)

lunch = ['baked beans']
add_spam(lunch)
print("The value of lunch = ", lunch)

print(add_spam())
print(add_spam())
print(add_spam())

#Solution:
def add_spam(menu=None):
    if menu is None:
        menu = []
    menu.append('spam')
    return menu

dinner = ['Momos']
add_spam(dinner)
print("The value of dinner = ", dinner)

print(add_spam())
print(add_spam())
