# ## line structure and indentation

import math

x = 0
y = 0
n = 0

# line continuation with "\"
a = math.cos(3 * (x - n)) + \
    math.sin(3 * (y - n))

# not needed with:
myString = """
no continuation character...
"""

myTuple = (
    "no continuation character"
)

myList = [
    "no continuation character"
]

myDict = {
    "foo": "no continuation character"
}

# indentation
# initial indent is arbitrary, but following must be consistent
if True:
    print("true")
else:
    print("false")

if True:
        print("true")
else:
        print("false")

# for short statements, they can be placed on same line
# (although it is a linter error)
if True: print("true")  # noqa: E701
else: print("false")    # noqa: E701


# identifiers starting with a single underscore are not imported with
# "from module import *"

# identifiers starting with a double underscore used to implement private
# class members

# ## NUMERIC LITERALS

# four types:
# * booleans
# * integers
# * floating point
# * complex

int(True)  # evaluates to 1
int(False)  # evaluates to 0

# octal  - start with "0o"
x = 0o12

# hex - start with "0x"
y = 0x12AC

# binary - start with "0b"
z = 0b10101

# integers in Python can have an arbitrary number of digits
x = 123456789012345678901234567890

# floating point
y = 123.45
y = 1.2345e+02

# floating point with trailing "j" or "J" is imaginary;
# to make a complex number:
c = 1.2 + 3.45j

# ## string literals

# no semantic difference between ', ", and """
# ', and " must be defined on a single line

# adjacent strings are concatenated to form a single strings
"one"    "two"     "three"  "four"  # evaluates to "onetwothreefour"

# backslash "\" is used to escape special characters

# in python 3, all strings are Unicode
