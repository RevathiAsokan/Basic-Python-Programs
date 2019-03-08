""" To find the number of combinations to choose k items from n items"""

from math import factorial as fact  # or use import math

""" n: 
        Total number of items
    k:
        Number of items to choose
    c:
        Number of combinations = n!/(k!*(n-k)!) """

n = int(input("Enter the total number of items: "))
k = int(input("Enter the number of items to choose: "))

c = (fact(n)/(fact(k)*fact(n-k)))  # or use c = (math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))

print("The total number of combinations to choose {0} items from {1} items is {2}".format(k, n, c))
