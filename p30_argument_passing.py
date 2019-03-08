""" Argument passing """

""" Type 1: if you write a function to modify copy of 
object, it is the responsibility of the function
to copy it """
print("Type 1: ")
m = [9, 15, 24]
print("The value of m : ", m)
def modify(k):
    k.append(39)
    print("k = ", k)
modify(m)
print("The value of m after modify() : ", m)

""" Type 2: To modify the contents of a list"""
print("\nType 2: ")
f = [14, 23, 27]
print("The value of f: ", f)
def replace_contents(g):
    g[0] = 17
    g[1] = 28
    g[2] = 45
    print("g = ", g)
replace_contents(f)
print("The value of f after modify: ", f)


""" Type 3: Pass by Object reference """
print("\nType 3:")
def f(d):
    return d
c = [6, 10 ,16]
e = f(c)
print("The value of c : ", c)
print("The value of e : ", e)
if c is e:
    print("c is e")
