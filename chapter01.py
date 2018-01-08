# ## RUNNING PYTHON
# working interactively in the REPL, '_' holds the result of the last operation

# start .py file with shebang interpreter directive to run as an executable:
# #!/usr/local/bin/python

# program can explicitly request an exit via:
# raise SystemExit

# ## VARIABLES AND ARITHMETIC EXPRESSIONS
# dynamically typed language
# - assignment operator creates association between a name and a value
# - each value has an associated typed
# - variable names are _untyped_ and can be made to refer to any type during
#   execution

# e.g.
# first, assign an int to x
x = 42

# next, assign a string to the same variable name
x = "forty two"

# although newline typically ends a statement, semicolon can be used as well
# note that mult. stmts. on one line is considered an error in Flake8
x = 3
y = 4

# OR
# x = 5; y = 6

# "while" tests condition and executes contained block iteratively while
# condition is true
while x > 0:
    x -= 1

# body of loop denoted by indentation
# - amt required is not specified
# - must be 'consistent'
# - recommendation: 4 spaces per level

# one approach for formatting output: string format operator
print("%3d %0.2f" % (2018, 123.4567))
# displays: "2018 123.46"

# uses special formatting-characters specifying type of data, and modifiers
# to specify width, precision, etc.
# "%d" (int), "%s" (string), "%f" (float)
# "%d3" - right aligned int with width 3
# "%0.2f" - float with only 2 digits after decimal point

# another approach is to use the `format` function;
# notice that the '%' are left off the format specifiers
print(format(2018, "3d"), format(123.4567, "0.2f"))

# third approach is to use the `format` method of strings, to format multiple
# values at once.
# (the number before the colon indicates the index of the argument to `format`;
# if excluded, then arguments are formatted in sequence)
print("{1:3d} {0:0.2f}".format(123.4567, 2018))
print("{:3d} {:0.2f}".format(2018, 123.4567))

# ## CONDITIONALS

# "if" and "else" perform simple tests
# bodies of if/else clauses denoted by indentation
# "else" is optional
# "pass" can be used to create an empty clause
if x > y:
    pass
else:
    print("x is not greater than y")

# use "or", "and", and "not" to form boolean expressions
if (x > 5 and y < 3) or x == 2:
    print("success!")

# backslash ("\") can be used to continue a statement on the next line
# indentation rules aren't applied to lines immediately following backslash

# use "elif" for multiple test cases
if(x == 0):
    print("zero")
elif(x == 1):
    print("one")
else:
    print("something else")

# use "True" and "False" to denote Boolean values
is_done = False

# relational operators ("==", ">", "<", return "True" or "False")
is_done = x > 5 or y < 2

# ## FILE INPUT AND OUTPUT

# "open" returns a new file object
f = open("./chapter01.py")

# "readline" reads a single line of input with trailing newline
# at EOF, and readline returns an empty string
line = f.readline()
while line:
    print(line, end='')
    line = f.readline()
f.close()

# the "for" statement can provide a simpler means for iterating over lines
f = open("./chapter01.py")
for line in f:
    print(line, end='')
f.close()

# a file can be provided to the print statement to write to a file
# note: the file must be opened for writing using the 'w' flag
f = open("./output.txt", 'w')
print("some example output", file=f)
f.close()

# files expose a "write" method to do the same something
f = open("./output.txt", 'w')  # note: this will overwrite the current version
f.write("some example output, v2\n")
f.close()

# standard output and input streams also provide functionality similar to files
import sys  # noqa: E402
sys.stdout.write("Enter your name: ")
name = sys.stdin.readline()

# this can be shortened using "input"
name = input("Enter your name: ")

# ## STRINGS

# string literals can be created using single, double, or triple quotes
a = 'Hello'
b = "World"
c = """I said "Hello"!"""

# triple quotes allow internal line-breaks and quote characters without escapes
c = """one
 two
  three
   four"""

# characters and fragments can be extracted from strings via indexing / slicing
a = "Hello World"
b = a[4]  # "o"
c = a[1:3]  # "el"
d = a[:5]  # "Hello"
e = a[6:]  # "World"

# concatenate strings with "+"
f = d + e  # "HelloWorld"

# to convert strings to numeric values, use functions like "int" and "float"
a = "42"
b = "99"
c = int(a) + int(b)  # 141 (integer, not string)

# convert non-strings to strings with "str", "repr", or "format"
# - str: returns the "informal", nicely printable string representation
# -repr: returns the string representation you'd type into a program to
#       represent the object
a = 42
str(a)
repr(a)
format(a, "d")

# ## LISTS
vegetables = ["carrot", "lettuce", "broccoli", "pea"]

# indexing
veg = vegetables[1]  # access -> "lettuce"
vegetables[1] = "kale"  # update

# append
vegetables.append("onion")

# insert
vegetables.insert(2, "pepper")

# slicing
vegetables[:2]  # ["carrot", "kale"]
vegetables[3:5] = ["cauliflower", "green bean"]

# concatenate with "+"
letters = ["a", "b", "c"] + ["d", "e", "f"]

# create empty
mylist = []
mylist = list()

# can contain any kind of object, and multiple types within a single list
variety = [1, "two", 3.0, [4, 4.0, "four", 2 * 2], (5, 5, 5, 5, 5)]

# nested values can be referenced with indexing more than once
variety[3][2]  # "four"
