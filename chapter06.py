# Ch 6 - Functions and Functional Programming

# # Functions


def foo1(a, b):
    return "you gave me {} and {}".format(a, b)


# order and number of arguments must mach those given in function definition
# otherwise, a `TypeError` is raised

# default arguments
# - that param, and all following, are optional
# - valueas must be assigned to all optional params or `SyntaxError`
#   is generated


def foo2(a, b="(nothing)"):
    return "you gave me {} and {}".format(a, b)


# def foo3(a, b="blah", c):
#     pass
# produces:  SyntaxError: non-default argument follows default argument

# default parameters are set at time of definition, not evaluation:
x = 42


def foo3(a, b=x):
    return "you gave me {} and {}".format(a, b)


x = 100
print(foo3(99))

# >>> you gave me 99 and 42

# NOTE: using mutable objects as default values may lead to unintended behavior


def foo4(a=[]):
    return a


x = foo4()
x.append(42)
print(foo4())

# >>> [42]

# to resolve this, use a default of `None` and set to the mutable object
# within the body of the function:


def foo5(a=None):
    if a is None:
        a = []

    return a


x = foo5()
x.append(42)
print(foo5())

# >>> []

# *args syntax:
# - a function can accept a variable number of parameters if an asterisk is
# added to the last parameter name
# - all remaining arguments are placed into last param as a tuple


def foo6(a, *args):
    print(len(args), args)


foo6(1, 2, 3)  # >>> 2 (2, 3)
foo6(1, 2, 3, 4, 5, 6, 7)  # >>> 6 (2, 3, 4, 5, 6, 7)


# a tuple can be passed as an argument to a function that accepts
# a variable number of parameters using a similar function calling syntax

t = ('a', 'b', 'c', 'd')
foo6(99, *t)  # >>> 4 ('a', 'b', 'c', 'd')

# >>> RESUME @ Ch 6. Keyword Arguments
