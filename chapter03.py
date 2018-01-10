import sys

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
