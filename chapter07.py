# # Chapter 07 - Classes and Object-Oriented Programming

# ## The `class` Statement

# - a class is defined using the `class` statement:


class Foo:
    instance_count = 0

    def __init__(self, bar, baz):
        self.bar = bar
        self.baz = baz
        Foo.instance_count += 1

    def __del__(self):
        Foo.instance_count -= 1

    def print_details(self):
        print("Foo: (bar-{}, baz-{})".format(self.bar, self.baz))


# - values created during execution of class body are placed in an object
# - serves as a namespace
# - can access values as follows:

Foo.instance_count  # <<< class variable; shared across instances
Foo.__init__
Foo.__del__
Foo.print_details  # <<< instance method

# ## Class Instances

# - created by calling a class object as a function
# - creates a new instance that is passed to __init__
# - args to init are the new instance, along with params provided when calling
#   the class object as a function
f = Foo(123, "Hi")  # ==> invokes Foo.__init__(f, 123, "Hi")

# - attributes are saved by assigning to `self`
# - attributes are accessed off `self` via the . operator
# - search for attributes looks on instance first, then checks class

# ## Scoping Rules

# - within class methods, references to class attributes and methods
#   must be fully qualified;
#   this is because in python, variables are not explicitly declared;
#   when assigning `x = 42` within a class method, there's no way to determine
#   if the intent is to assign a local variable, or an instnace attribute

# ## Inheritance

# - mechanism for creating a new class that specializes / modifies the
#   behavior of an existing class
# - base class or superclass: original class
# - derived class or subclass: new, specialized class
# - specified with comma-separated list of base-class names in `class` stmt
# - by default, classes inherit from `object`


class DemoBase():
    def say_hi(self):
        print("hello from DemoBase")


class DemoDerived1(DemoBase):
    def say_hi(self):
        print("hello from DemoDerived1")


class DemoDerived2(DemoBase):
    # this one will pick up fx from parent
    pass


d1 = DemoDerived1()
d1.say_hi()

d2 = DemoDerived2()
d2.say_hi()

# >>> hello from DemoDerived1
# >>> hello from DemoBase

# - override support implemented by modifying search path of `.` operator:
#   - searches first in derived instances methods/attributes
#   - if not found, works its way up through parents until found

# - when derived class defines `__init__`, the `__init__` method on base class
#   is not automatically invoked; derived class must call the method explicitly:


class DemoBaseInit():
    def __init__(self, x):
        self.x = x


class DemoDerivedInit1(DemoBaseInit):
    def __init__(self, x, y):
        self.y = y
        DemoBaseInit.__init__(self, x)


class DemoDerivedInit2(DemoBaseInit):
    # without the explicit call to the base class's `__init__`
    # method, this class won't have an `x` attribute defined
    def __init__(self, y):
        self.y = y


def format_demo_derived_init(d):
    return """
    x: {},
    y: {}
    """.format(d.x, d.y)


d1 = DemoDerivedInit1(11, 22)
print("d1: {}".format(format_demo_derived_init(d1)))

# >>> d1:
# >>>     x: 11,
# >>>     y: 22

d2 = DemoDerivedInit2(22)
print("d2: {}".format(format_demo_derived_init(d2)))

# >>> AttributeError                            Traceback (most recent call last)  # noqa
# >>> <ipython-input-11-ab850a388e95> in <module>()
# >>>       1 d2 = DemoDerivedInit2(22)
# >>> ----> 2 print("d2: {}".format(format_demo_derived_init(d2)))
# >>>
# >>> <ipython-input-9-9d213050a49e> in format_demo_derived_init(d)
# >>>      19     x: {},
# >>>      20     y: {}
# >>> ---> 21     """.format(d.x, d.y)
# >>>
# >>> AttributeError: 'DemoDerivedInit2' object has no attribute 'x'


# - similarly, a derived class can call a base class implementation of
#   a method to access that functionality

class DemoBaseMethod1():
    def say_hi(self):
        print("hello from base")


class DemoDerivedMethod1(DemoBaseMethod1):
    def say_hi(self):
        print("hello from derived")
        DemoBaseMethod1.say_hi(self)


d1 = DemoDerivedMethod1()
d1.say_hi()

# >>> hello from derived
# >>> hello from base

# - if what's needed is to call the nearest parent's version of  a method,
#   a more dynamic approach to doing that would be to use the `super` function:


class DemoDerivedMethod2(DemoBaseMethod1):
    def say_hi(self):
        print("hello from derived v2")
        super().say_hi()


d2 = DemoDerivedMethod2()
d2.say_hi()

# >>> hello from derived v2
# >>> hello from base

# ## multiple inheritance

# - specified by providing comma separated list of multiple base classes


class Root1:
    def run1(self):
        print("hello from root 1")

    def shared(self):
        print("shared method - root 1")


class Root2():
    def run2(self):
        print("hello from root 2")

    def shared(self):
        print("shared method - root 2")


class Child1(Root1, Root2):
    pass


c1 = Child1()
c1.run1()
c1.run2()
c1.shared()

# >>> hello from root 1
# >>> hello from root 2
# >>> shared method - root 1

# if the order of based classes were reversed above (i.e. Root2, Root1),
# the call to `shared` would have run the version defined in Root2

# this is based on the method resolution order
# to see the order in which methods are resolved, see `.mro`:
Child1.mro()

# >>> [__main__.Child1, __main__.Root2, __main__.Root1, object]

# ## Polymorphism, Dynamic Binding, and Duck Typing

# dynamic binding - the capability to use an instance without regards to its
#    type

# looking up an attribute will work on any object that _has_ that attribute
# this is known as "duck typing": if it looks like, quacks like, and walks
#   like a duck, then it's a duck

# customized versions of objects can be made by creating a new object
# that supports all the attributes and methods of the source object

# ## Static Methods and Class Methods

# static method - a function that lives in the namespace dfined by a class
#   defined using the `@staticmethod` decorator
#   called against the class itself:  MyClass.dosomething()

# class method - operators on the class itself, as an object
#   defined using the `@classmethod` decorator
#   when called, the class is passed as the first argument (rather than `self`)


class Root2():
    def display(self):
        print("hello from root2")

    @staticmethod
    def get_v1():
        return Root2()

    @classmethod
    def get_v2(cls):
        return cls()


class Child2(Root2):
    def display(self):
        print("hello from child2")


Root2.get_v1().display()
Root2.get_v2().display()
Child2.get_v1().display()
Child2.get_v2().display()

# >>> hello from root2
# >>> hello from root2
# >>> hello from root2
# >>> hello from child2

# note that static and class methods can also be called on instances of
# the classes they're defined on:

c2 = Child2()
c2.get_v1().display()
# >>> hello from root2

# # Properties

# - special kind of attribute that computes its value when accessed
# - `@property` keyword allows access without need for trailing `()`


class SpecialNumber:
    def __init__(self, value):
        self.value = value

    @property
    def double(self):
        return self.value * 2

    def display_with(self, x):
        print("{}, {}".format(self.value, x))


n = SpecialNumber(42)
print("n.value: {}".format(n.value))
print("n.double: {}".format(n.double))

# >>> n.value: 42
# >>> n.double: 84

# - attribute also prevents re-assigning the value
n.double = 66

# >>> -------------------------------------------------------------------------
# >>> AttributeError                          Traceback (most recent call last)
# >>> <ipython-input-6-d0c9ae2c46f8> in <module>()
# >>> ----> 1 n.double = 66
# >>>
# >>> AttributeError: can't set attribute

# - accessing a non-attributed method using similar syntax returns
#   a bound method:
#   - an object representing the function call to execute via `()`
#   - sim. to a partially evaluated function with the `self` param evaluated
#   -  additional args supplied with `()`
#   - created automatically via an internal property function
# - `@staticmethod` and `@classmethod` indicate the use of _different_
#   property functions
#   - e.g. `@staticmethod` indicates to return the method back "as-is"

n.display_with

# >>> <bound method SpecialNumber.display_with of <__main__.SpecialNumber object at 0x109856b38>>  # noqa

# ## property setters and deleters


class SimpleValue:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        print("setting value to {}".format(new_value))
        self.__value = new_value

    @value.deleter
    def value(self):
        # simulate deletion
        print("deleting value")
        self.__value = "DELETED"


s = SimpleValue("hello")
print("s.value: {}".format(s.value))

s.value = "goodbye"
print("s.value: {}".format(s.value))

del s.value
print("s.value: {}".format(s.value))

# >>> s.value: hello
# >>> setting value to goodbye
# >>> s.value: goodbye
# >>> deleting value
# >>> s.value: DELETED

# ## descriptors

# - a further generalization of support for properties / attribute access on a class
# - simply an object that represents the value of an attribute
#   - can customize behavior of getters / setters by implementing special methods:
#   - `__get__()`
#   - `__set__()`
#   - `__delete__()`

class DescriptorProperty(object):
    def __init__(self, name, value):
        self.name = "_" + name
        self.default = value
        print("in __init__")

    def __get__(self, instance, cls):
        print("in __get__")
        return getattr(instance, self.name, self.default)

    def __set__(self, instance, value):
        print("in __set__")
        setattr(instance, self.name, value)

    def __delete__(self, instance):
        print("in __delete__")


class Foo(object):
    p1 = DescriptorProperty("p1", "hi")
    p2 = DescriptorProperty("p2", "bye")


f = Foo()
    
f.p1

# >>> in __get__
# >>> "hi"

f.p1 = "hello"

# >>> in __set__
