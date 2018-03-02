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

# >>> RESUME @ Scoping Rules <<<
