'''
if (3 < 2):
    print("3 is more than 2")
else:
    print("3 is not more than 2")

if (3 < 3):
    print("option 1")
elif (3 == 3):
    print("option 2")
else:
    print("option 3")

letter = "u"
if 0:
    print("got a")
elif (letter == "b"):
    print("got b")
else:
    print("got something else")
'''
def print_stuff():
    print("a function is printing this")
    print("isn't that cool?!")

print_stuff() 

def operation(a, b, c):
    return a**2 + b/4 - c

print(operation(3, 4, 2))


# this function has a return
def hello(n):
    return n*"Hello Ellyn "
#print(hello(1000))

# 2 * w + 2 * h 
# 2 * (w + h)
def rectangle_perimeter(w, h):
    return w + w + h + h 

def rectangle_area(w, h):
    return w * h

def rectangle_info(width, height, x):
    if x == "a":
        return rectangle_area(width, height)
    elif x == "p":
        return rectangle_perimeter(width, height)
    else:
        return -1
print(rectangle_info(35, 500, "a"))

print(rectangle_perimeter(35, 400))
print(rectangle_area(35, 400))


# this function does not return anything
'''
multi
line
comment
'''
def hi(n):
    print(n*'hi')

#print(hello(100))