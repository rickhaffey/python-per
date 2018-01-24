# ## Mathematical Operators


class SpecialString:
    def __init__(self, value):
        self.value = value

    # The following methods can be defined to emulate numeric objects. Methods
    # corresponding to operations that are not supported by the particular kind
    # of number implemented (e.g., bitwise operations for non-integral numbers)
    # should be left undefined.

    # These methods are called to implement the binary arithmetic operations
    #   (+, -, *, @, /, //, %, divmod(), pow(), **, <<, >>, &, ^, |). For
    #   instance, to evaluate the expression x + y, where x is an instance
    #   of a class that has an __add__() method, x.__add__(y) is called.
    #   The __divmod__() method should be the equivalent to using
    #   __floordiv__()
    #   and __mod__(); it should not be related to __truediv__(). Note that
    #   __pow__() should be defined to accept an optional third argument if the
    #   ternary version of the built-in pow() function is to be supported.

    def __add__(self, other):  # +
        pass

    def __sub__(self, other):  # -
        pass

    def __mul__(self, other):  # *
        pass

    def __matmul__(self, other):  # @
        pass

    def __truediv__(self, other):  # /
        pass

    def __floordiv__(self, other):  # //
        pass

    def __mod__(self, other):  # %
        pass

    def __divmod__(self, other):  # divmod()
        pass

    def __pow__(self, other, modulo=None):  # pow() or **
        pass

    def __lshift__(self, other):  # <<
        pass

    def __rshift__(self, other):  # >>
        pass

    def __and__(self, other):  # &
        pass

    def __xor__(self, other):  # ^
        pass

    def __or__(self, other):  # |
        pass


# object.__radd__(self, other)
# object.__rsub__(self, other)
# object.__rmul__(self, other)
# object.__rmatmul__(self, other)
# object.__rtruediv__(self, other)
# object.__rfloordiv__(self, other)
# object.__rmod__(self, other)
# object.__rdivmod__(self, other)
# object.__rpow__(self, other)
# object.__rlshift__(self, other)
# object.__rrshift__(self, other)
# object.__rand__(self, other)
# object.__rxor__(self, other)
# object.__ror__(self, other)

# These methods are called to implement the binary arithmetic
# operations (+, -, *, @, /, //, %, divmod(), pow(), **, <<, >>, &, ^, |)
# with reflected (swapped) operands. These functions are
# only called if the left operand does not support the
# corresponding operation [3] and the operands are of different
# types. [4] For instance, to evaluate the expression x - y,
# where y is an instance of a class that has an __rsub__()
# method, y.__rsub__(x) is called if x.__sub__(y) returns NotImplemented.
#
# Note that ternary pow() will not try calling __rpow__()
# (the coercion rules would become too complicated).
#
# Note If the right operand’s type is a subclass of the
# left operand’s type and that subclass provides the
# reflected method for the operation, this method will
# be called before the left operand’s non-reflected method.
# This behavior allows subclasses to override their ancestors’ operations.

# object.__iadd__(self, other)
# object.__isub__(self, other)
# object.__imul__(self, other)
# object.__imatmul__(self, other)
# object.__itruediv__(self, other)
# object.__ifloordiv__(self, other)
# object.__imod__(self, other)
# object.__ipow__(self, other[, modulo])
# object.__ilshift__(self, other)
# object.__irshift__(self, other)
# object.__iand__(self, other)
# object.__ixor__(self, other)
# object.__ior__(self, other)

# These methods are called to implement the augmented
# arithmetic assignments
# (+=, -=, *=, @=, /=, //=, %=, **=, <<=, >>=, &=, ^=, |=).
# These methods should attempt to do the operation in-place
# (modifying self) and return the result (which could be,
# but does not have to be, self). If a specific method is
# not defined, the augmented assignment falls back to the
# normal methods. For instance, if x is an instance of a
# class with an __iadd__() method, x += y is equivalent
# to x = x.__iadd__(y) . Otherwise, x.__add__(y) and
# y.__radd__(x) are considered, as with the evaluation of
# x + y. In certain situations, augmented assignment can
# result in unexpected errors
# (see Why does a_tuple[i] += [‘item’] raise an exception
# when the addition works?), but this behavior is in
# fact part of the data model.
#
# object.__neg__(self)
# object.__pos__(self)
# object.__abs__(self)
# object.__invert__(self)
# Called to implement the unary arithmetic operations (-, +, abs() and ~).
#
# object.__complex__(self)
# object.__int__(self)
# object.__float__(self)
# object.__round__(self[, n])
# Called to implement the built-in functions complex(), int(),
# float() and round(). Should return a value of the appropriate type.
#
# object.__index__(self)
# Called to implement operator.index(), and whenever Python
# needs to losslessly convert the numeric object to an integer
# object (such as in slicing, or in the built-in bin(), hex()
# and oct() functions). Presence of this method indicates that
# the numeric object is an integer type. Must return an integer.
#
# Note In order to have a coherent integer type class, when
# __index__() is defined __int__() should also be defined,
# and both should return the same value.
