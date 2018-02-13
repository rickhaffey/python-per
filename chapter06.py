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

# keyword arguments
# - order (in call) doesn't matter
# - must name all non-optional params
# - if any required are omitted, or if names mismatch : TypeError


def foo7(x, y, z):
    print("you passed {}, {}, and {}".format(x, y, z))


foo7(x=1, y=42, z="hello")  # >>> you passed 1, 42, and hello


# can combine positional and named:
# - positional must come first
# - all non-optional args are provided
# - none are provided more than 1x
foo7("bar", "bat", z="baz")  # >>> you passed bar, bat, and baz


# kwargs
# - supported if last param named **{param_name}
# - provided as a dictionary


def foo8(x, y, **kwargs):
    print("you passed: {}, {}, and {}".format(x, y, kwargs))


foo8(42, 99, bar="bar", bat="bat", baz=100)
# >>> you passed: 42, 99, and {'bar': 'bar', 'bat': 'bat', 'baz': 100}

# *args + **kwargs


def foo9(*args, **kwargs):
    print("you passed: {} and {}".format(args, kwargs))


foo9(1, 42, 99, x=1.23, y=0.5, z="hell")
# >>> you passed: (1, 42, 99) and {'x': 1.23, 'z': 'hell', 'y': 0.5}

# ## Parameter Passing and Return Values
# - no simple pass-by-value or pass-by-reference
# - depends on type of argument passed
#   - immutable: similar to pass-by-value
#   - mutable: similar to pass-by-reference


def foo10(x):
    x[1] = 42


z = [1, 2, 3]
print(z)
foo10(z)
print(z)

# >>> [1, 2, 3]
# >>> [1, 42, 3]

# above is an example of a method with side effects
# more functional approach would _not_ modify the original
# and instead return a copy

# values are returned via `return`
# functions without a return yield `None`
# can use tuples to return multiple values

# ## Scoping Rules

# - new local namespace created for function execution
# - contains fx params and locals
# - resolution searches (in order):
#   - local
#   - global (module in which function is defined)
#   - built-in
#   - not found => `NameError`

# `global` keyword
# - inside a function, variable references by default are to local vars
# - variables named the same as globals will be treated as new local vars
# - to instead refer to the global var, use the `global` keyword:
g = 100


def foo11():
    g = 42
    print("g inside fx: {}".format(g))


print("g before fx: {}".format(g))
foo11()
print("g after fx: {}".format(g))

# >>> g before fx: 100
# >>> g inside fx: 42
# >>> g after fx: 100


# using `global` keyword
g = 100


def foo12():
    global g
    g = 42
    print("g inside fx: {}".format(g))


print("g before fx: {}".format(g))
foo12()
print("g after fx: {}".format(g))

# >>> g before fx: 100
# >>> g inside fx: 42
# >>> g after fx: 42


# nested function definitions
# - lexical scoping: resolution works upward through nested levels
# - use `nonlocal` keyword to modify a non-global variable from a higher
# - only applies at 1 level -- does not apply to further nested variables
#   containing scope:


def foo13():
    x = 99

    def foo14():
        x = 100
        print("foo14(): {}".format(x))

    print("foo13(): {}".format(x))
    foo14()
    print("foo13(): {}".format(x))


foo13()
# >>> foo13(): 99
# >>> foo14(): 100
# >>> foo13(): 99


def foo15():
    x = 99

    def foo16():
        nonlocal x
        x = 100
        print("foo16(): {}".format(x))

    print("foo15(): {}".format(x))
    foo16()
    print("foo15(): {}".format(x))


foo15()

# >>> foo15(): 99
# >>> foo16(): 100
# >>> foo15(): 100

# attempts to use a local variable before assignment: `UnboundLocalError`


def foo17():
    print(i)
    i = 42


foo17()
# >>> UnboundLocalError: local variable 'i' referenced before assignment

# >>> RESUME @ Functions as Objects and Closures
