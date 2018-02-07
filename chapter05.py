# Ch 05 - Program Structure and Control Flow

# Conditional Execution

check1 = check2 = False

if check1:
    print("check 1")
elif check2:
    print("check 2")
elif False:
    pass  # use `pass` if there's not statement for a given clause
else:
    print("none of the above")

# Loops / Iteration

while check1:
    pass

# `for` works with any object supporting iteration:
# - list, tuple, string, etc.
# - anything implementing iterator protocol
for x in [1, 2, 3]:
    pass


class RoundTripIterator:
    def __init__(self, values):
        self.values = values
        l = list(range(len(self.values)))
        l.extend(l[-2::-1])

        self.indices = l
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if(self.index < len(self.indices)):
            result = self.values[self.indices[self.index]]
            self.index += 1
            return result
        else:
            raise StopIteration


class Foo:
    def __init__(self, values):
        self.values = values

    def __iter__(self):
        return RoundTripIterator(self.values)


for f in Foo([1, 2, 3]):
    print(f)

# >>> 1
# >>> 2
# >>> 3
# >>> 2
# >>> 1

# the for loop above is effectively doing the following:
it = Foo([1, 2, 3]).__iter__()  # `it` is the iteration variable
while 1:
    try:
        f = it.__next__()
        print(f)
    except StopIteration:
        break

# elements can be unpacked as part of for loop:
for x, y in [(1, 2), (3, 4), (5, 6)]:
    print("x: {}, y: {}".format(x, y))

# >>> x: 1, y: 2
# >>> x: 3, y: 4
# >>> x: 5, y: 6

# `enumerate` function maps elements of a collection to their 0 based indices:
alpha = "ABCD"
for (i, a) in enumerate(alpha):
    print("i: {}, a:{}".format(i, a))

# >>> i: 0, a:A
# >>> i: 1, a:B
# >>> i: 2, a:C
# >>> i: 3, a:D

# `zip` function maps elements of two (or more) collections
r = range(4)
l = [x ** 2 for x in r]
for (a, x, xsq) in zip(alpha, r, l):
    print("a: {}, x: {}, x-squared: {}".format(a, x, xsq))

# >>> a: A, x: 0, x-squared: 0
# >>> a: B, x: 1, x-squared: 1
# >>> a: C, x: 2, x-squared: 4
# >>> a: D, x: 3, x-squared: 9

# for unequal size collections, the smallest determines zipped result:
l1 = [1, 2, 3]
l2 = [1, 3, 5, 7, 9]
for x, y in zip(l1, l2):
    print("x: {}, y:{}".format(x, y))

# >>> x: 1, y:1
# >>> x: 2, y:3
# >>> x: 3, y:5

# `break` jumps out of loop
for i in range(10):
    if i == 3:
        break
    print(i, end=',')

# >>> 0,1,2,

# `continue` jumps to the next iteration
for i in range(10):
    if i % 2 == 0:
        continue

    print(i, end=',')

# >>> 1,3,5,7,9,

# break and continue only apply to innermost loop being executed

# `else` against loops - only executed if loop runs to completion
from random import random  # noqa
for i in range(10):
    print(i, end=',')
    lucky = random() > 0.90
    if lucky:
        break
else:
    print("bang!")

# run 1: >>> 0,1,2,
# run 2: >>> 0,1,2,3,4,5,6,7,8,9,bang!

# Exceptions

# raise Exception([value])
raise RuntimeError()
raise ValueError("The value for foo must be non-negative.")

# raise by itself raises the last exception generated
try:
    1 / 0
except Exception:
    # re-raise the caught exception
    raise

# >>> ZeroDivisionError: division by zero


try:
    print("dividing by zero")
    1 / 0
    print("won't ever hit this")
except ZeroDivisionError:
    print("caught the error")

print("outside the try block")

# >>> dividing by zero
# >>> caught the error
# >>> outside the try block

# uncaught exceptions can be passed to user-defined function
# via sys.excepthook
import sys  # noqa


def custom_handler(type, value, traceback):
    print("Type: {}".format(type))
    print("Value: {}".format(value))
    print("Traceback: {}".format(traceback))


sys.excepthook = custom_handler

# raise an uncaught exception
1 / 0

# >>> Type: <class 'ZeroDivisionError'>
# >>> Value: division by zero
# >>> Traceback: <traceback object at 0x105e83208>

# `except as {var}`
try:
    raise ValueError("boo")
except ValueError as ex:
    print(repr(ex))

# >>> ValueError('boo',)

# multiple except blocks
try:
    1 / 0
except ValueError:
    print("value error")
except IOError:
    print("i/o error")
except ZeroDivisionError:
    print("zero div error")
except RuntimeError:
    print("runtime error")
except Exception:
    print("some other unexpected error")

# >>> zero div error

# multiple exception types per handler:
try:
    1 / 0
except (ValueError, IOError, ZeroDivisionError):
    print("specific expected error")
except (RuntimeError):
    print("general expected error")
except Exception:
    print("unexpected error")

# >>> specific expected error

# ignore exceptions via pass:
try:
    1 / 0
except Exception:
    pass

# use `Exception` to catch all except those related to program exit
# to catch _all_ exceptions, use `except` with no exception type
# - avoid this, as it also catches keyboard interrupts, reqs for prog. exit,
#   etc.

# `try ... else`


def try_else(denom):
    try:
        print("before")
        1 / denom
        print("after")
    except Exception:
        print("caught")
    else:
        print("else block")


try_else(1)

# >>> before
# >>> after
# >>> else block

try_else(0)

# >>> before
# >>> caught

# `try ... finally`


def try_else_finally(denom):
    print("entering")
    try:
        print("before")
        1 / denom
        print("after")
    except Exception:
        print("caught")
    else:
        print("else block")
    finally:
        print("finally block")

    print("exiting")


try_else_finally(1)

# >>> entering
# >>> before
# >>> after
# >>> else block
# >>> finally block
# >>> exiting

try_else_finally(0)

# >>> entering
# >>> before
# >>> caught
# >>> finally block
# >>> exiting


def finally_no_catch(denom):
    try:
        print("before")
        1 / denom
        print("after")
    finally:
        print("in finally block")


finally_no_catch(1)

# >>> before
# >>> after
# >>> in finally block

finally_no_catch(0)

# >>> before
# >>> in finally block
# >>> ZeroDivisionError: division by zero


# >>> RESUME @ Ch 5. - Built-in exceptions <<<
