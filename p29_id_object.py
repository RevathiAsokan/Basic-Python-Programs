""" id() deals with the object, not the reference
    Value - equivalent "contents"
    identity - same object """

p = [4, 7, 11]
q = [4, 7, 11]
print("Value of p = {0}, ID of p = {1}".format(p, id(p)))
print("Value of q = {0}, ID of q = {1}".format(q, id(q)))

if p == q:
    print("P is equal to Q")

if p is not q:
    print("Id of p and q is different")
