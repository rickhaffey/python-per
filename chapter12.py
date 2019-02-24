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

# bytearray([x]) - Type representing a mutable array of bytes.
# x can be one of the following
# - sequence of integers in the range 0 to 255
# - an 8-bit string or bytes literal
# - an integer representing the size of the array
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