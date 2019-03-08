""" To demonstrate For loop"""

print("For in List")
cities = ["London", "New York", "Paris", "Oslo", "Helsinki"]
for city in cities:
    print(city)

print("\nFor in Dictionaries")
phone_book = {'Akhil': '896-897-5689', 'Raaj': '459-789-2356', 'Harsh': '456-789-123'}
for phone in phone_book:
    print(phone,phone_book[phone])

print("\nHexadecimal input to decimal output")
colors = {'crimson': 0xdc143c, 'coral': 0xff7f50, 'teal': 0x008080}
for color in colors:
    print(color, colors[color])
