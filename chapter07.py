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
#   is not automatically invoked; derived class must call the method
#   explicitly:


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

# ## Descriptors
#  https://docs.python.org/3/howto/descriptor.html

# - a further generalization of support for properties / attribute access on a
#   class
# - simply an object that represents the value of an attribute
#   - can customize behavior of getters / setters by implementing special
#     methods:
#   - `descr.__get__(self, obj, type=None) --> value`
#   - `descr.__set__(self, obj, value) --> None`
#   - `descr.__delete__(self, obj) --> None`
#   define any of these methods, and an object is considered a descriptor

# with get+set, object is a data descriptor
#    if set raises exception, it's a read-only data descriptor
# with get but no set, object is a non-data descriptor

# methods can be called:
# - directly: `d.__get__(obj)`, or
# - more common, indirectly: `obj.d` ; behind the scenes, this is a call
#    to `type(obj).__dict__['d'].__get__(obj, type(obj))`

# important notes
# - descriptors are invoked by the `__getattribute__()` method
# - overriding `__getattribute__()` prevents automatic descriptor calls
# - `object.__getattribute__()` and `type.__getattribute__()`
#    make different calls to `__get__()`
# - data descriptors always override instance dictionaries.
# - non-data descriptors may be overridden by instance dictionaries.

# the `property` decorator is essentially creating descriptors for the
# decorated attributes


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

# ## Data Encapsulation and Private Attributes

# - by default, all attributes and methods of a class are public
# - all names in a class that start with a double underscore
#   are automatically mangled to form a new name:
#   - `_{className}__{attributeName}`


class PrivateMethods:
    def __init__(self):
        self.value = 42

    def __foo(self):
        print("Foo: {0:d}".format(self.value))

    def bar(self):
        print("Bar: {0:d}".format(self.value))


p = PrivateMethods()
p.bar()
# >>> Bar: 42

p.__foo()
# >>> ---------------------------------------------------------------------------  # noqa
# >>> AttributeError                            Traceback (most recent call last)  # noqa
# >>> <ipython-input-2-36635920d6ac> in <module>()
# >>> ----> 1 p.__foo()
# >>>
# >>> AttributeError: 'PrivateMethods' object has no attribute '__foo'

# note that this is just an "illusion" of data hiding; the attribute can be
# accessed using the mangled name:

p._PrivateMethods__foo()
# >>> Foo: 42


# see the `SimpleValue` example above as a good example of using private
# values in combination with properties to support encapsulation

# Object Memory Management

# object instantiation
# - call to `__new__()` => creates new instance
#   - rarely defined by user code
#   - class method
#   - if defined in a class, usually means either,
#     - the class is inheriting from an immutable base class
#     - the class is defining a metaclass
# - call to `__init__()` => initializes instance

class NewExample:
    @classmethod
    def __new__(cls, *args, **kwargs):
        print("in def...")
        return super(NewExample, cls).__new__(cls)

    def __init__(self):
        print("in init...")


ne = NewExample()
# >>> in def...
# >>> in init...

# is the same as

ne2 = NewExample.__new__(NewExample)
if(isinstance(ne2, NewExample)):
    NewExample.__init__(ne2)
# >>> in def...
# >>> in init...

# - instances are managed by reference counting
# - when about to be destroyed, the interpreter looks for
#   a `__del__()` method, and calls it
# - note that the `del` method doesn't directly
#   call `__del__()`
# - risky to rely on `__del__()` for a clean shutdown;
#   consider having app explicitly call a method intended
#   for shutdown
# - reference cycles can lead to memory leaks
#   - this can sometimes be solved by using `weakref`


class DelExample:
    def __del__(self):
        print("in __del__()")


def f_del():
    d = DelExample()  # noqa
    # ref count should go to 0 here


f_del()
# >>> in __del__()


# weakref example
import weakref  # noqa


class WeakRefExample:
    def __init__(self, foo):
        self.foo = weakref.ref(foo)

    def display(self):
        foo = self.foo()  # <- notice fx call syntax
        if foo:
            foo.print_details()
        else:
            print("foo: NA")


def f_wr():
    foo = Foo(1, 2)
    wr = WeakRefExample(foo)
    wr.display()
    return wr


wr = f_wr()
wr.display()

# >>> Foo: (bar-1, baz-2)
# >>> foo: NA

# Object Representation and Attribute Binding

# ## `__dict__`
# - instances represented internally as a dictionary : `__dict__`


class DictDemo:
    def __init__(self, value1, **kw):
        self.value1 = value1


dd = DictDemo(42)
print(dd.__dict__)
# >>> {'value1': 42}

# add another value using prop syntax, it's reflected in dict
dd.value2 = "hello"
print(dd.__dict__)
# >>> {'value1': 42, 'value2': 'hello'}

# or using the dict directly
dd.__dict__['value3'] = 3
print(dd.__dict__)
# >>> {'value1': 42, 'value2': 'hello', 'value3': 3}

# ## `__class__`
# instances linked back to their class via `__class__`
print(dd.__class__)
# >>> <class '__main__.DictDemo'>

# this class also has a __dict__ attribute containing attributes
# of the class, including methods, etc.
print(dd.__class__.__dict__)
# >>> {'__module__': '__main__', '__init__': <function DictDemo.__init__ at 0x107dc9598>,  # noqa
# >>> '__dict__': <attribute '__dict__' of 'DictDemo' objects>,
# >>> '__weakref__': <attribute '__weakref__' of 'DictDemo' objects>, '__doc__': None}     # noqa


# ## `__bases__`
# a class has a special attribute (__bases__) linking it to its
# base classes
# - tuple of the base classes


class OtherDemo:
    def __init__(self, foo, bar, **kw):
        self.foo = foo
        self.bar = bar


class BasesDemo(DictDemo, OtherDemo):
    def __init__(self, value1, foo, bar):
        super(BasesDemo, self).__init__(value1=value1, foo=foo, bar=bar)


bd = BasesDemo(42, "FOO", "bar")
print(bd.__class__.__bases__)
# >>> (<class '__main__.DictDemo'>, <class '__main__.OtherDemo'>)

# ## setters and getters
# - `obj.name = value` invokes `obj.__setattr__("name", value)`
#    - default handling is to modify that value in dict
#    - if "name" refers to a descriptor, invokes set method of descriptor
# - `del obj.name` invokes `obj.__delattr__("name")`
#    - default handling to delete value from dict
#    - if "name" refers to a descriptor, invokes delete method of descriptor
# - retrieval of `obj.name` invokes `obj.__getattr__("name")`
#    - search path:
#    - properties,
#    - local __dict__,
#    - class __dict__,
#    - searching the base classes
#    - __getattr__ method of the class (if defined)
#    - AttributeError

# - a class can re-implement __getattr__, __setattr__, and __delattr__
#   - they should usually rely on the behavior implemented in `object`
#     to carry out the actual work

# ## __slots__
# - the `__slots__` attribute is used to restrict set of legal instance
#   attribute names
# - performance mechanism; improves memory use and execution time
#   over classes that use dict to store attributes
# - that said, it can cause issues with inheritance, leading to
#   worse performance if base class(es) don't _also_ define a
#   `__slots__` values


class SlotsDemo:
    __slots__ = ("one", "two")


s = SlotsDemo()
s.one = 1
s.two = 2
s.three = 3
# >>> ---------------------------------------------------------------------------
# >>> AttributeError                            Traceback (most recent call last)
# >>> <ipython-input-2-0f2b14b29514> in <module>()
# >>> ----> 1 s.three = 3
# >>> 
# >>> AttributeError: 'SlotsDemo' object has no attribute 'three'

s.__dict__
# >>> ---------------------------------------------------------------------------
# >>> AttributeError                            Traceback (most recent call last)
# >>> <ipython-input-3-eb17e9874e77> in <module>()
# >>> ----> 1 s.__dict__
# >>> 
# >>> AttributeError: 'SlotsDemo' object has no attribute '__dict__'

# ## Operator Overloading
# user defined classes can overload standard math operators, etc via operator
# overloading
# - `__add__`
# - `__sub__`


class OpOverloadDemo:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return OpOverloadDemo(self.value + other.value)

    def __sub__(self, other):
        return OpOverloadDemo(self.value - other.value)

    def __str__(self):
        return "value: {}".format(self.value)


v1 = OpOverloadDemo(1)
v2 = OpOverloadDemo(2)
vresult = v1 + v2
print(vresult)
# >>> value: 3

# robust support for operators requires handling type coercion for
# mismatched lhs and rhs types, etc.

# ## Types and Class Membership Tests

# - `isinstance(obj, cname)`
#   returns True if `obj` is an instance of `cname` or of a type
#   derived from `cname`
# - `issubclass(A, B)`
#   returns True if `A` is a subclass of `B`

print("isinstance(v1, OpOverloadDemo): {}".format(isinstance(v1, OpOverloadDemo)))
# >>> isinstance(v1, OpOverloadDemo): True

foo = Foo(1, 2)
print("isinstance(foo, OpOverloadDemo): {}".format(isinstance(foo, OpOverloadDemo)))
# >>> isinstance(foo, OpOverloadDemo): False


class Root:
    pass


class Branch1(Root):
    pass


class Branch2(Root):
    pass


class Leaf(Branch1, Branch2):
    pass


print(issubclass(Branch1, Root)) # True
print(issubclass(Branch1, Root)) # True
print(issubclass(Leaf, Root)) # True
print(issubclass(Root, Leaf)) # False

# behavior of these two methods can be overridden with
# - `__instancecheck__`, and
# - `__subclasscheck__`
# to support duck-typing scenarios where a class doesn't
# match type constraints, but does match functional
# "contract" constraints

# Abstract Base Classes

# - defined using the `abc` module
#   - `ABCMeta`, `@abstractmethod`, `@abstractproperty`
#   - cannot be instantiated directly
#   - requires methods and properties to be implemented in derived classes
#   - doesn't check params on methods
#   - it can define concrete methods to be used in derived classes

from abc import ABCMeta, abstractmethod, abstractproperty
class AbstractDemo(metaclass=ABCMeta):
    @abstractmethod
    def foo(self, a, b):
        pass

    @abstractproperty
    def bar(self):
        pass

    def bat(self):
        print("bat in AbstractDemo")


a = AbstractDemo()
# >>> --------------------------------------------------------------------------
# >>> TypeError                                 Traceback (most recent call last)
# >>> <ipython-input-2-406544d0f1a2> in <module>()
# >>> ----> 1 a = AbstractDemo()
# >>> 
# >>> TypeError: Can't instantiate abstract class AbstractDemo with abstract methods bar, foo    


class ConcreteDemo(AbstractDemo):
    def foo(self, a, b):
        print("foo in ConcreteDemo: {}, {}".format(a, b))

    @property
    def bar(self):
        return "bar"


c = ConcreteDemo()
c.foo(1, 2)
# >>> foo in ConcreteDemo: 1, 2
c.bar # >>> 'bar'
c.bat()
# >>> bat in AbstractDemo

# - pre-existing classes can be registered to belong to abstract base class
#   via the `register` method


class RegisterDemo():
    pass

AbstractDemo.register(RegisterDemo)

rd = RegisterDemo()
issubclass(RegisterDemo, AbstractDemo) # >>> True

# note that registration _didn't_ check to ensure that the registered
# class implements the required abstract methods and properties

# - built-in types are under a relatively flat hierarchy (based on `Object`)
# - ABC module allows user-driven organization of existing classes into
#   custom hierarchy for app specific purposes

# ## Metaclasses

# - a metaclass is an object that knows how to create and manage classes
# - default metaclass of user defined classes is `type`

class MetaDemo():
    pass

# class definition _itself_ becomes an object
isinstance(MetaDemo, object) # >>> True

type(MetaDemo) # >>> type

# when a new class is defined, the following code steps occur:
class_name = "MetaDemo"
class_parents = (object,)
class_body = "pass"
class_dict = {}

exec(class_body, globals(), class_dict)

MetaDemo = type(class_name, class_parents, class_dict)

# we could create a class taking the same steps explicitly

class_name = "MetaDemo2"
class_parents = (object,)
class_body = """
def display(self):
    print("displaying MetaDemo2")
"""
class_dict = {}

exec(class_body, globals(), class_dict)

MetaDemo2 = type(class_name, class_parents, class_dict)

# ----

m2 = MetaDemo2()
m2.display() # >>> displaying MetaDemo2

# the last step of the above process, where `type` is invoked,
# can be customized by providing a metaclass in the base classes
# defined on a class; e.g.:
# `class MetaDemo2(metaclass=type): pass`

# - metaclass resolution chain:
#   - if `metaclass` provided in class base classes, use that
#   - look at first base class type provided, use metaclass of that
#   - look for a global `__metaclass__` variable, use that
#   - finally, it will use the default `__metaclass__` value
#     (`type()` in P3)

# primary use of metaclasses is to allow asserting more control over
# the definition of user defined objects
# e.g.:
# - require that all public methods are documented
# - inspecting and gathering information about class definitions
# - alter contents of class def prior to class creation

# note: avoid using metaclasses to define functionality that
# doesn't adhere to the normal coding rules expected for classes

# ## Class Decorators

# used to perform some kind of extra processing after a class is
# defined
#
# class decorator: a function that take a class as input and
#   returns a class as output


def log_class(cls):
    print("class created: {}".format(cls.__clsid__))
    return cls


@log_class
class ClassDecDemo():
    __clsid__ = "some_id"

# >>> class created: some_id
    


