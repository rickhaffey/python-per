# coding=utf-8
# # Chapter 12 - Built-in Functions and Exceptions

# ## Built-in Functions and Types

# abs(x) - absolute value
p = 1234
n = -1234
print("abs(p): {}".format(abs(p)))
print("abs(n): {}".format(abs(n)))
# >>> abs(p): 1234
# >>> abs(n): 1234

# all(s) - return True if all elements of s evaluate to True
s = [True, True]
print("all({}): {}".format(s, all(s)))
s = [True, False]
print("all({}): {}".format(s, all(s)))
# >>> all([True, True]): True
# >>> all([True, False]): False

# any(s) - return True if any elements of s evaluate to True
s = [False, False]
print("any({}): {}".format(s, any(s)))
s = [False, True]
print("any({}): {}".format(s, any(s)))
# >>> any([False, False]): False
# >>> any([False, True]): True

# ascii(x) - like `repr()`, but only using ASCII chars; non-ASCII turned
#            into appropriate escape sequences
ex = "German lowercase letter 'ß'"
print("ascii({}): {}".format(ex, ascii(ex)))
print("repr({}): {}".format(ex, repr(ex)))
# >>> ascii(German lowercase letter 'ß'): "German lowercase letter '\xdf'"
# >>> repr(German lowercase letter 'ß'): "German lowercase letter 'ß'"

# bin(x) - returns a string containing the binary representation of integer x
x = 42
print("bin({}): {}".format(x, bin(x)))
# >>> bin(42): 0b101010

# bool(x) - Type representing Boolean values; converts x to True/False;
#           called with no args returns False
print("bool({}): {}".format("", bool()))
print("bool({}): {}".format(0, bool(0)))
print("bool({}): {}".format(1, bool(1)))
print("bool({}): {}".format([], bool([])))
print("bool({}): {}".format(['hi'], bool(['hi'])))
print("bool({}): {}".format("", bool("")))
print("bool({}): {}".format("bye", bool("bye")))
# >>> bool(): False
# >>> bool(0): False
# >>> bool(1): True
# >>> bool([]): False
# >>> bool(['hi']): True
# >>> bool(): False
# >>> bool(bye): True

# breakpoint() - Drop into the debugger

breakpoint()
# >>> --Call--
# >>> > ~/.../lib/python3.7/site-packages/IPython/core/displayhook.py(247)__call__()
# >>> -> def __call__(self, result=None):

# bytearray([source[, encoding[, errors]]]) - Type representing a mutable array of bytes.
# source can be one of the following
# - sequence of integers in the range 0 to 255
# - a string, with an optional encoding (default is utf-8) and encoding error handling scheme
# - an integer representing the size of the array
# - an object conforming to the `buffer` interface
y = [0, 1, 2, 3, 4, 5]
print("bytearray({}): {}".format(y, bytearray(y)))
# >>> bytearray([0, 1, 2, 3, 4, 5]): bytearray(b'\x00\x01\x02\x03\x04\x05')
y = b'\x04\x02'
print("bytearray({}): {}".format(y, bytearray(y)))
# >>> bytearray(b'\x04\x02'): bytearray(b'\x04\x02')
y = 3
print("bytearray({}): {}".format(y, bytearray(y)))
# >>> bytearray(3): bytearray(b'\x00\x00\x00')


# - can index to get an integer value representing the byte value at index
y = bytearray([10, 20, 30, 40])
x = y[3]
print("x: {}".format(x))
# >>> x: 40

# - can update values by assigning integer byte value
print("y: {}".format(y))
y[3] = 42
print("y: {}".format(y))
# >>> y: bytearray(b'\n\x14\x1e(')
# >>> y: bytearray(b'\n\x14\x1e*')

# - provides all operations associated with strings
#   (preface all strings with `b`)

# bytes([x]) -- Type representing an immutable array of bytes.
# - an immutable version of `bytearray`
# - sim arguments to that method
y = [0, 1, 2, 3, 4, 5]
print("bytes({}): {}".format(y, bytes(y)))
# >>> bytes([0, 1, 2, 3, 4, 5]): b'\x00\x01\x02\x03\x04\x05'

# main diff: immutable
# - attempts to update fail:
y = bytes([10, 20, 30, 40])
print("y: {}".format(y))
y[3] = 42
print("y: {}".format(y))


# >>> y: b'\n\x14\x1e('
# >>> ---------------------------------------------------------------------------
# >>> TypeError                                 Traceback (most recent call last)
# >>> <ipython-input-12-ab9ad72fa478> in <module>
# >>>       1 y = bytes([10, 20, 30, 40])
# >>>       2 print("y: {}".format(y))
# >>> ----> 3 y[3] = 42
# >>>       4 print("y: {}".format(y))
# >>>
# >>> TypeError: 'bytes' object does not support item assignment

# callable(object) - returns True if the object appears callable, False if not

def demo_function():
    print('demo')


print("callable(demo_function): {}".format(callable(demo_function)))
print("callable(42): {}".format(callable(42)))
# >>> callable(demo_function): True
# >>> callable(42): False

# ====================

# chr(x)
# classmethod(func)
# cmp(x, y)
# compile(string, filename, kind [, flags [, dont_inherit]])
# complex([real [, imag]])
# delattr(object, attr)
# dict([m])
# dict(key1 = value1, key2 = value2, ...)
# dir([object])
# divmod(a, b)
# enumerate(iter [, initial_value])
# eval(expr [, globals [, locals]])
# exec(code [, global [, locals]])
# filter(function, iterable)
# float([x])
# format(value [, format_spec])
# frozenset([items])
# getattr(object, name [, default])
# globals()
# hasattr(object, name)
# hash(object)
# help(object)
# hex(x)
# id()
# input([prompt])
# int(x [, base])
# isinstance(object, classobj)
# issublclass(class1, class2)
# iter(object [, sentinel])
# len(s)
# list([items])
# locals()
# long([x [, base]])
# map(function, items, ...)
# max(x [, args, ...])
# memoryview()
# min(s [, args, ...])
# next(s [, default])
# object()
# oct(x)
# open(filename [, mode [, bufsize [, encoding [, errors [, newline [, closefd]]]]]])
# open(filename [, mode [, bufsize]])
# ord(d)
# pow(x, y [, z])
# print(value, ... [, sep=separator, end=ending, file=outfile])
# property([fget [, fset [, fdel [, doc]]]])
# range([start, ] stop [, step])
# raw_input([prompt])
# repr(object)
# reversed(s)
# round(x [, n])
# set([items])
# setattr(object, name, value)
# slice([start, ] stop [, step])
# sorted(iterable [, key=keyfunc [, reverse=reverseflag]])
# staticmethod(func)
# str([object])
# sum(items [, initial])
# super(type [, object])
# tuple([items])
# type(name, bases, dict)
# unichr(x)
# unicode(string [, encoding [, errors]])
# vars([object])
# xrange([start, ] stop [, step])
# zip([s1 [, s3 [, ...]]])
# __import__()
