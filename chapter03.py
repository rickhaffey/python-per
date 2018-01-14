# ## 3. Types and Objects

# every piece of data stored in a py program is an Objects
# each object has a
# - identity (pointer to a loc. in memory)
# - type (class)
# - value

# identity and type can't be changed after instantiation
# if value can be changed, object is mutable, otherwise, it's immutable

# object that contains refs to other objects: container or collection

# attribute: value associated with an object
# method: function associated with an object
# both accessed using dot (.) notation

# ## object identity and type
# `id()` function returns identity of object as integer
#  - usually the mem location, but implementation specific
x = 42
print("id of x: {}".format(id(x)))

# `is` compares identity of two objects


class Foo:
    def __eq__(self, other):
        # treat all Foo's as value-equal
        return True


a = Foo()
b = Foo()

print("id of a: {}".format(id(a)))
print("id of b: {}".format(id(b)))
print("a == b: {}".format(a == b))
print("a is b: {}".format(a is b))

# `type()` returns the type of an object
print("type(x): {}".format(type(x)))
print("type(a): {}".format(type(a)))

# type of an object is _itself_ an object: the object's class
# - uniquely defined
# - always the same for all instances of a given type
# - can be compared using the `is` operator
# - assigned names can be used for type checking
print("type(a) is type(b): {}".format(type(a) is type(b)))
print("type([]) is list: {}".format(type([]) is list))

# a better way to check is to use `isinstance`
# - inheritance aware
print("isinstance([], list): {}".format(isinstance([], list)))

# arguments against heavily using type checking:
# - can negatively affect performance
# - could miss interfaces of objects that don't match hierarchy but support
#   protocol
# - heavy usage can be a sign that design needs to be reconsidered

# ## reference counting and garbage collection
# - all objects are reference-counted
#   - ref count is increased whenever an object is assigned to a new name or
#     placed in a container
a = 37  # < ref count for object with value 37 = 1
b = a  # < ref count = 2
c = []
c.append(b)  # < ref count = 3

# - ref count is decreased by
#   - `del` statement
#   - reference goes out of scope
#   - name is re-assigned
del a  # < ref count for value 37 = 2
b = 42  # < ref count = 1
c[0] = 2.0  # < ref count = 0

# current reference count can be obtained with `sys.getrefcount`:

import sys  # noqa : E402


def print_a_refs():
    print("sys.getrefcount(a): {}".format(sys.getrefcount(a)))


a = 37
print_a_refs()
b = a
print_a_refs()
del b
print_a_refs()

# note: value might be higher than expected:
# - interpreter shares immutable objects across project to conserve memory
# - etc.

# when an object's ref count reaches 0, it is garbage-collected

# circular dependencies:
# in example below, ref count for q and r won't drop to 0 even after `del`
# statements, resulting in a memory leak

# interpreter periodically searches for such inaccessible objects and deletes
# them
q = {}
r = {}
q['r'] = r
r['q'] = q
del q
del r


# ## references and copies
a = [1, 2, 3, 4]
b = a  # b now points to the same object that a points to
b[2] = 42  # this changes the same underlying object behind both 'a' and 'b'
print(a[2])  # 42

# two types of copy operations

# - shallow copy: new object, but populates it with references to the same
#       items contained in the original objects
a = [1, 2, [3, 4]]
b = list(a)  # creates a shallow copy
print("b is a: {}".format(b is a))

# appending/removing to a shallow copy doesn't affect original
b.append(42)
print("a: {}".format(a))
print("b: {}".format(b))

# modify a (mutable) object contained by the copy will change the object in the
# original, too
b[2][1] = 99
print("a: {}".format(a))
print("b: {}".format(b))

# - deep copy: creates a new object, and recursively copies all the objects
#       it contains
#   - no built-in operation
#   - use `copy` module in standard library: `copy.deepcopy`
import copy  # noqa : E402
a = [1, 2, [3, 4]]
b = copy.deepcopy(a)
b[2][1] = 43
print("a: {}".format(a))
print("b: {}".format(b))

# ## first-class objects
# - all objects that can be named by an identifier have equal status
# - all objects that can be named can be treated as data
data = {}

# basic
data["number"] = 42  # int
data["text"] = "hello"  # string

# more complex
data["func"] = abs  # builtin function
data["mod"] = sys  # module
data["error"] = ValueError  # type
data["append"] = a.append  # function of another object

# this allow for compact, flexible code
line = "GOOG,100,490.10"
types = [str, int, float]
fields = [ty(val) for ty, val in zip(types, line.split(","))]
print(fields)

# ## built-in types for representing data:

# ### The `None` Type
#   `type(None)` - The null object `None`
# - denotes a null object
# - exactly 1
# - often used to indicate when default params aren't overridden in function
#    call
# - has no attributes
# - evaluates to False in Boolean expressions

# ### Numeric Types
#   `int` - integer
#       - whole numbers
#       - range: unlimited (except by available memory)
#       - acts like py2 `long` type
#   `float` - floating point
#       - represented using native double-precision (64-bit) rep of machine
#       - typically this is IEEE 754
#         - approximately 17 digits of precision
#         - exponent in the range –308 to 308
#         - same as `double` type in C
#       - for more precise space / precision control, look to using numpy
#   `complex` - complex number
#       - represented as pair of floating-point numbers
#       - `z.real` : real portion
#       - `z.imag` : imaginary part
#   `bool` - Boolean
#   - two values: (`True` => 1 or `False` => 0)
# - all immutable
# - all (except Boolean) are signed
# - to support a common interface / mixed arithmetic, some shared attributes:
#   - x.numerator (int)
#   - x.denominator (int)
#   - x.real (int + float)
#   - x.imag (int + float)
#   - x.conjugate (int + float)
#   - x.as_integer_ratio (float)
#   - x.is_integer (float)
# - additional numeric types in library modules (e.g. `decimal`, `fractions`,
#   etc.)

# >>>> RESUME HERE <<<<<

# ### Sequences

# - ordered sets of objects indexed by integers
# - support iteration
#   `str` - character string
#       - sequence of characters
#       - immutable
#   `list` - list
#       - sequence of arbitrary python objects
#       - allow insertion, deletion, substitution
#   `tuple` - tuple
#       - sequence of arbitrary python objects
#       - immutable
#   `range` - a range of integers

# operations available on all sequences:
a = [1, 2, 3, 4, 5]
a[3]
a[2:4]
a[1:5:2]
len(a)
min(a)
max(a)
sum(a)
all(a)  # checks whether all are true
any(a)  # checks whether any are true

# operations available on mutable sequences (e.g. lists)
a[3] = 42
a[2:4] = [99] * 2
a[1:5:2] = [1001] * 2
del a[3]
del a[2:4]
del a[1:5:2]

# ### lists

# convert an iterable to a list with `list()`
# - if iterable is already a list, creates a shallow copy
i = range(3)
a = list(i)
a.append(42)
a.extend([43, 44, 45])
a.count(42)  # counts occurrences of 42 in a
a.index(42)  # returns index of first instance of 42 found in a
a.insert(3, 99)  # insert 99 at index 3
a.pop()
a.remove(99)
a.reverse()  # reverse (in place)


def strange_sort(x):
    if(x <= 3):
        return x
    else:
        return -x


a.sort(key=strange_sort, reverse=True)
print(a)

# ### Mapping
#   `dict` - dictionary

# ### Sets
#   `set` - mutable set
#   `frozenset` - immutable set
