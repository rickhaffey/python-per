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


# >>> RESUME @ multiple inheritance <<<
