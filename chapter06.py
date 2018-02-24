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

# ## Functions as Objects and Closures

# closure - when the statements that make up a function are packaged with
#           the environment in which they execute

# - all functions have a `__globals__` attribute that points to the global
#   namespace in which the function was defined (e.g. the enclosing module
#   in which a function was defined

# useful for delayed execution
# - define a function that returns another function, that will be called
#   at some later time, but use the context of the point of creation

# it's possible to view the contents of the variables carried in a closure:


def simple(x, y):
    print("x: {}".format(x))
    print("y: {}".format(y))


def outer(param):
    def inner():
        simple(param, param ** 2)
    return inner


f = outer(2)

f()
# >>> x: 2
# >>> y: 4

print(f.__closure__[0].cell_contents) # >>> 2

# ## Decorators
# - function that wraps another function or class
# - purpose is to alter or enhance behavior of the wrapped object
# - denoted using '@'


def log_before_after(func):
    def callf(*args, **kwargs):
        print("before")
        r = func(*args, **kwargs)
        print("after")
        return r

    return callf


@log_before_after
def decorator_demo(x):
    print("you passed in '{}'".format(x))


decorator_demo(42)

# >>> before
# >>> you passed in '42'
# >>> after

# note - this is shorthand syntax for the equivalent:
#
#    def decorator_demo(x):
#        print("you passed in '{}'".format(x))
#    decorator_demo = log_before_after(decorator_demo)

# more than one decorator can be applied to a function, and will be "evaluated"
# in the order applied

# decorators can accept arguments


def log_prefix(prefix):
    def log_before_after(func):
        def callf(*args, **kwargs):
            print(prefix + " " + "before")
            r = func(*args, **kwargs)
            print(prefix + " " + "after")
            return r

        return callf

    return log_before_after


@log_prefix("HI!")
def decorator_demo2(x):
    print("you passed in '{}'".format(x))


decorator_demo2(99)

# >>> HI! before
# >>> you passed in '99'
# >>> HI! after

# equivalent to:
#
# def decorator_demo2(x):
# ...
# temp = log_prefix("HI!")
# decorator_demo2 = temp(decorator_demo2)

# decorators can be applied to class definitions


def addId(original_class):
    # capture the original init
    orig_init = original_class.__init__

    def __init__(self, id, *args, **kwargs):
        self.__id = id
        self.get_id = lambda: self.__id

        # call the original
        orig_init(self, *args, **kwargs)

    # re-assign init on the decorated class
    # to our new version
    original_class.__init__ = __init__
    return original_class


@addId
class Decoratee:
    def __init__(self):
        print("inside init...")
        print("id is :{}".format(self.get_id()))


d = Decoratee(123)
# >>> inside init...
# >>> id is :123

# ## Generators and `yield`
# - a function using `yield` produces a generator
# - a generator is a function producing a sequence of values for use
#    in iteration


def count_by(increment=1, start=0, stop=50):
    x = start
    while x <= stop:
        yield x
        x += increment


c = count_by(5)
c.__next__()
# >>> 0

c.__next__()
# >>> 5

c.__next__()
# >>> 10

[c for c in count_by(5)]
# >>> [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# call to `__next__` executes up to the `yield` statement, producing the next
# result

# subsequent calls to `__next__` resume execution at the point _after_ `yield`

# the generator signals completion by raising a `StopIteration` exception

# a shutdown can be signaled before generator is complete via
# the `close` method:

c = count_by(3)
print(c.__next__())
print(c.__next__())
c.close()
print(c.__next__())

# >>> 0
# >>> 3
# >>> ---------------------------------------------------------------------------  # noqa
# >>> StopIteration                             Traceback (most recent call last)  # noqa
# >>> <ipython-input-35-88bd522ad2be> in <module>()
# >>>       3 print(c.__next__())
# >>>       4 c.close()
# >>> ----> 5 print(c.__next__())
# >>>
# >>> StopIteration:

# inside generator, `close` is signaled via a `GeneratorExit` exception:


def count(start):
    x = start
    while True:
        try:
            yield x
            x += 1
        except GeneratorExit:
            print("catching a GeneratorExit")


c = count(3)
print(c.__next__())
print(c.__next__())
c.close()
print(c.__next__())

# >>> 3
# >>> 4
# >>> catching a GeneratorExit
# >>> --------------------------------------------------------------------------- # noqa
# >>> RuntimeError                              Traceback (most recent call last) # noqa
# >>> <ipython-input-37-bcfe83be3ee2> in <module>()
# >>>       2 print(c.__next__())
# >>>       3 print(c.__next__())
# >>> ----> 4 c.close()
# >>>       5 print(c.__next__())
# >>>
# >>> RuntimeError: generator ignored GeneratorExit

# Note: ignoring the GeneratorExit and continuing to yield values after a
# call to `close` is a violation of the generator protocol, as noted by
# the RuntimeError and corresponding message indicated above.

# >>> RESUME @ Coroutines and `yield` Expressions <<<
