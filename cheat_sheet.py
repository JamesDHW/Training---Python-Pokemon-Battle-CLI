# ====================== SIMPLE DATA TYPES ======================
# Python is 'dynamically typed' meaning it guesses the data type (implicit declaration)
integer = 1
string = "1"
decimal = 1.0  # 'Float'
boolean = True  # Or 'False'

# print and type functions
print("Print values and types of values")
print(integer, string, decimal, boolean)  # Converts all to string and prints separating with a space
print(type(integer), type(string), type(decimal), type(boolean))

# Casting to other data types
print("\nPrint values and types of values after casting to int")
print(integer, int(string), int(decimal), int(boolean))
print(type(integer), type(int(string)), type(int(decimal)), type(int(boolean)))

print("\nPrint values and types of values after casting to str")
print(str(integer), string, str(decimal), str(boolean))
print(type(str(integer)), type(string), type(str(decimal)), type(str(boolean)))

print("\nPrint values and types of values after casting to float")
print(float(integer), float(string), float(decimal), float(boolean))
print(type(float(integer)), type(float(string)), type(decimal), type(float(boolean)))

print("\nPrint values and types of values after casting to bool (1==True,0==False)")
print(bool(integer), bool(string), bool(decimal), bool(boolean))
print(type(bool(integer)), type(bool(string)), type(bool(decimal)), type(boolean))
print()

# ======================     OPERATORS      =====================
two = 2
ten = 10
fifteen = 15
print("2 x 2 =", two * two)
print("2 ^ 2 =", two ** two)
print("10 ^ 2 =", ten ** two)
print("10 + 10 =", ten + ten)
print("15 - 10 =", fifteen - ten)
print("remainder: 10 % 2 =", ten % two)
print("remainder: 15 % 2 =", fifteen % two)
print("remainder: 15 % 10 =", fifteen % ten)
print("floor division: 10 // 2 =", ten // two)
print("floor division: 15 // 2 =", fifteen // two)
print("floor division: 15 // 10 =", fifteen // ten)
print()

# ====================== COMPLEX DATA TYPES ======================
# Useful for dynamically sized variables
# List - any data type, element(s) found by indexing (or slicing)
ls = [integer, string, decimal, boolean]
print("list:", ls)
print("first element ls[0]:", ls[0], "\nsecond element ls[1]:", ls[1], "\nlast element ls[-1]", ls[-1])
print("list slice, first two ls[:2]", ls[:2], "\nslice ls[2:]", ls[2:], "\nreverse slice ls[-2:-1]", ls[-2:-1])

# Dictionary - key of any simple data type, any value, elements found by key
dct = {1: integer, '2': string, 3.0: decimal, True: boolean}
print("dictionary:", dct)
print("value at key 1, dct[1]:", dct[1])
print("value at key True, dct[True]:", dct[True])

# Tuple - same as list but values are unchangeable (immutable)
tup = (integer, string, decimal, boolean)
print("tuple:", tup, type(tup))
# Set - unordered (no indexing) + no duplicates
st = {integer, string, decimal, boolean}
print("set:", st, type(st))
print()

# ====================== CONDITIONAL STATEMENTS ======================
# These evaluate to either True or False, which is all that Python reads for these statements


print("Conditional operators are: ==, !=, <, >, <=, >=, and, or, not, in, is\n")
print("True == True is", True == True)
print("True == False is", True == False)
print("1 == 1 is", 1 == 1)
print("1 == 0 is", 1 == 0)
print()
print("True != True is", True != True)
print("True != False is", True != False)
print("1 == 1 is", 1 != 1)
print("1 == 0 is", 1 != 0)
print()
print("1 > 2 is", 1 > 2)
print("1 > 2 is", 1 > 2)
print("1 >= 2 is", 1 >= 2)
print("1 <= 2 is", 1 <= 2)
print()
print("True and True and True and True is", True and True and True and True)
print("True and True and True and False is", True and True and True and False)
print()
print("True or False is", True or False)
print("False or False is", False or False)
print()
print("not False is", not False)
print("not True is", not True)
print()
x = [1, 2, 3];
y = x
print("x = [1,2,3]; y=x; x is y", x is y, "(exact object match)")
print("[1,2,3] is [1,2,3]", [1, 2, 3] is [1, 2, 3], "(don't share same memory location)")
print("1 in [1,2,3]", 1 in [1, 2, 3])
print("4 in [1,2,3]", 4 in [1, 2, 3])

# ====================== CONDITIONAL PROGRAMMING ======================


condition = True
if condition:
    print("if statement activated for True condition")

condition = False
if condition:
    pass  # does nothing
else:
    print("else statement activated for False condition")

condition2 = True
if condition:
    pass  # does nothing
# can have as many as we want
elif condition2:
    print("elif statement activated for second condition True")

condition2 = False
if condition:
    pass  # does nothing
elif condition2:
    pass  # does nothing
else:
    print("else statement activated where all other conditions False")

print()
print("====================== WHILE LOOPS ======================")
# ====================== WHILE LOOPS ======================


while True:
    print("will loop whiles top condition is True")
    break  # Use break to avoid infinite loop

while False:
    print("code never reached")

increment = 0
while increment < 10:
    increment += 1
    print(increment)

print("increment reset to 0")
increment = 0
while increment < 10:
    increment += 1
    continue  # Skips extra code and tests again
    print(increment)
print("looped 10x didn't print each time due to continue", increment)
print()

print("====================== FOR LOOPS ======================")
# ====================== FOR LOOPS ======================


# Loops for as many elements in the list
for i in [1, 2, 3]:
    print(i)

# Loops over range(3)
for i in range(3):
    print(i + 1)

# Range can have different start, stop, and increments
for i in range(6, 13, 2):
    print(i)

# Loops for all elements, i is the index of the list
for i in range(len([1, 2, 3])):
    print(i + 1)

print()
print("====================== TRY-EXCEPT ======================")
# ====================== TRY-EXCEPT ======================


try:
    int("sausage")
except:
    print("ran into an error casting 'sausage' to an integer")

try:
    str(1996)
    print("successful casting to string")
except:
    print("ran into an error casting")

# More complex
# If you know what might go wrong and want to check quickly then do something else
try:
    float(23)
except:
    pass
else:
    print("succeeded, now doing other non-dangerous code")

print()
print("====================== FUNCTIONS ======================")


# ====================== FUNCTIONS ======================
# Abstraction is an essential concept - build up your own toolbox of functions to reuse


def add(a, b):
    return a + b


print("add(2, 2) is", add(2, 2))
print("add(3, 3) is", add(3, 3))
print("add(4, 4) is", add(4, 4))
print()


def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False


print("isEven(0) is", isEven(0))
print("isEven(1) is", isEven(1))
print("isEven(2) is", isEven(2))
print("isEven(3) is", isEven(3))


print()
print("====================== MODULES/ LIBRARIES ======================")


# ====================== MODULES/ LIBRARIES ======================
# Sometimes we want to use functions which someone else has written instead of writing our own
import numpy
import pandas as pd
import matplotlib.pyplot as plt

print("numerical python zeros array:\n", numpy.zeros((5, 5)))
print("pandas and matplotlib to create a plot (un-comment 'plt.show()')")
ts = pd.Series(numpy.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
plt.show()


print()
print("====================== OBJECTS ======================")


# ====================== OBJECTS ======================
# ADVANCED TOPIC

class mammal():
    def __init__(self):
        self.variable = True
        pass

    def walkMethod(self):
        # some walking behaviour
        pass

    @staticmethod
    def eatStaticMethod():
        # some eating behaviour
        pass


# Inherits behaviour from mammal
class human(mammal):
    def __init__(self, name):
        self.name = name
        print(self.name)
        pass


James = human("James")
Jack = human("Jack")
