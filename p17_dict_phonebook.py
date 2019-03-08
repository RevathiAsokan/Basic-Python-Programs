""" Phone book using dictionaries"""

phone_books = {'Anand': '745-986-7845'}

size = input("Enter the number of contacts you wish to add")

for i in range(1, 100, 1):
    response = input("Would you like to add contact (yes/no: ")
    if response == 'yes' and i <= int(size):
        name = input("Enter name: ")
        phone_books[name] = input("Enter contact no.")
    else:
        print("Done with adding or Exceeded Limit")
        break

print("You have added {0} contacts out of {1}".format(int(i-1), size))
print("Phone book: {}".format(phone_books))
print("Phone book: ")

for phone in phone_books:
    print(phone, phone_books[phone])
