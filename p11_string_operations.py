""" String operations
    To accept your name, position and print the letter in that position in Caps"""

name = input("Enter your name: ")
letter_num = int(input("Enter the number of a letter: "))

character = name[letter_num - 1]
print("Type of character is: ", type(character))  # characters are simply one element strings

print('The letter at position {0} is {1}'.format(letter_num, character.capitalize()))
