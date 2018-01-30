# # Operators and Expressions

# ## Operations on Numbers

# - division:
# 10 / 3 => 3.3333
# 10 // 3 => 3 (truncates non-integral portion)
# 10 % 3  => 1 (modulo; produces remainder of division)
#       equivalent to `num - (num // denom) * denom`

# - bitwise ops (integers only)

# `<<`  # left shift
# `>>`  # right shift
# `&`   # bitwise and
# `|`   # bitwise or
# `^`   # bitwise xor
# `~`   # bitwise negation
template = "{}: 0b{:0>5b}"
a = 0b10100
b = 0b00101

print(template.format("a & b", a & b))
print(template.format("a | b", a | b))
print(template.format("a ^ b", a ^ b))

# - builtin functions

# abs
# divmod(x, y)  # => (x // y, x % y)
# pow(x, y, [, modulo])  # => (x ** y) % modulo
# round  # ties broken by rounding to nearest _even_ multiple
#        # 0.5 => 0,  1.5 => 2

# - comparisons
# - can be chained:


def lower():
    print('lower')
    return 10


def upper():
    print('upper')
    return 60


def x():
    print('x')
    return 42


lower() < x() < upper()
# evaluated as `(lower() < x()) and (x() < upper())`
# appears to be optimized in that second call to x() doesn't happen:

# result => True
# output:
#  >>> lower
#  >>> x
#  >>> upper

# for operations involving more than one number, operands are coerced
# to a 'common' type as follows
# 1) if either is complex, others are coerced to complex
# 2) else, if either is floating-point, others are coerced to floating-point
# 3) else, operands are integers and there's no coercion

# ## Operations on Sequences

s = "one two three"
l = ["one", "two", "three"]
t = ("one", "two", "three")

s + "four five"  # => 'one two threefour five'
l + ["four", "five"]  # => ['one', 'two', 'three', 'four', 'five']

[1, 2, 3] * 2  # => [1, 2, 3, 1, 2, 3]
2 * [1, 2, 3]  # => sim.

# note: shallow copies; replicated by reference

x, y, z = [1, 2, 3]  # => x = 1, y = 2, z = 3

# note: unpacking structure must match:
a, b = ((1, 2, 3), (4, 5, 6))  # => a = (1,2,3), b = (4,5,6), OR
(a, b, c), (d, e, f) = ((1, 2, 3), (4, 5, 6))  # => a=1,b=2,c=3,d=4,e=5,f=6
# not: a, b, c, d, e, f = ((1,2,3), (4,5,6))

# index / slice  : # l[i:j:stride]

# membership
"two" in t  # => True
"two" not in t  # => False

# note: strings also accept _sub-strings_ in addition to chars
"he" in "hello"  # => True

# iteration
for word in l:
    print(word)

# all()
# any()
# len()
# min()
# max()
# sum()


# ## List Modification

l = [1, 2, 3]
l[1] = 42  # => [1, 42, 3]
l[1:] = [99, 99]  # => [1, 99, 99]

# sequence is expanded or reduced to accomodate all the elements in r
l = [1, 2, 3]
l[1:2] = [99] * 3  # => [1, 99, 99, 99, 3]

l = [1, 2, 3]
l[1:] = []  # => [1]

# del
l = [1, 2, 3]
del l[1]  # => [1, 3]

l = [1, 2, 3]
del l[1:]  # => [1]

# sequence comparison
l1 = [1, 2, 3]
l2 = [1, 2, 4]

l1 < l2  # => True:  1 == 1, 2 == 2, 3 < 4

l1 = [1, 2, 3]
l2 = [1, 2, 3, 0]
l1 < l2  # => True: 1 == 1, 2 == 2, 3 == 3, no index 3 in l1

l1 = [1, 2, 4]
l2 = [1, 2, 3, 0]
l1 < l2  # => False: 1 == 1, 2 == 2, 4 > 3

# #string comparison
# - compared using lexicographical ordering
# - each chars numerical index is determined by the character set
# - characters ordered based on their index

# ordered comparison of byte and unicode strings will raise exception:
b'abc' < u'abc'  # => TypeError

# ## String Formatting

# - % formatting
# - similar to sprintf (C)
# - combines a format string and a tuple or map of objects

template = """
int: %d
unsigned int: %u
octal int: %o
hex int: %x
hex int (uppercase): %X
float: %f
float (sci. notation): %e
float (SCI. NOTATION): %E
float (sci for "large" exponents): %g
float (SCI for "large" exponents): %G
str(): %s
repr(): %r
char: %c
literal %%: %%
"""


class Foo:
    def __repr__(self):
        return "Foo() # repr()"

    def __str__(self):
        return "Foo # str()"


i = 42
f_s = 1.234
f_l = 1.234e10
o = Foo()
c = 120  # ord("x")
values = (i, i, i, i, i, f_s, f_l, f_l, f_l, f_l, o, o, c)
print(template % values)

# >>> int: 42
# >>> unsigned int: 42
# >>> octal int: 52
# >>> hex int: 2a
# >>> hex int (uppercase): 2A
# >>> float: 1.234000
# >>> float (sci. notation): 1.234000e+10
# >>> float (SCI. NOTATION): 1.234000E+10
# >>> float (sci for "large" exponents): 1.234e+10
# >>> float (SCI for "large" exponents): 1.234E+10
# >>> str(): Foo # str()
# >>> repr(): Foo() # repr()
# >>> char: x
# >>> literal %: %

# format with mapping
mapping = {
    "foo": Foo(),
    "bar": 1.234e10,
    "bat": 42
}

template = """
foo: %(foo)s
foo2: %(foo)r
bar: %(bar)E
bat: %(bat)X
"""

print(template % mapping)

# >>> foo: Foo # str()
# >>> foo2: Foo() # repr()
# >>> bar: 1.234000E+10
# >>> bat: 2A

# format alignments
pos = 12.345
neg = -1 * pos

template = """
right align (default): %(pos)40f
left align: %(neg)-40f

## include the sign:
right align: %(pos)+40f
left align: %(pos)-+40f
right align: %(neg)+40f
left align: %(neg)-+40f

## include zero fill:
right align: %(pos)040f
left align: %(pos)-040f
"""

print(template % {"pos": pos, "neg": neg})

# >>> right align (default):                                12.345000
# >>> left align: -12.345000
# >>>
# >>> ## include the sign:
# >>> right align:                               +12.345000
# >>> left align: +12.345000
# >>> right align:                               -12.345000
# >>> left align: -12.345000
# >>>
# >>> ## include zero fill:
# >>> right align: 000000000000000000000000000000012.345000
# >>> left align: 12.345000

# formatting precision
f = 12.345
s = "abcdefghij"
i = 42
template = """
%%(f).1f: %(f).1f
%%(f).2f: %(f).2f
%%(f).3f: %(f).3f
%%(f).4f: %(f).4f
%%(f).5f: %(f).5f

%%(s).3s: %(s).3s
%%(s).4s: %(s).4s
%%(s).5s: %(s).5s

%%(i).1i: %(i).1i
%%(i).2i: %(i).2i
%%(i).3i: %(i).3i
%%(i).4i: %(i).4i
"""

print(template % {"f": f, "s": s, "i": i})

# >>> %(f).1f: 12.3
# >>> %(f).2f: 12.35
# >>> %(f).3f: 12.345
# >>> %(f).4f: 12.3450
# >>> %(f).5f: 12.34500
# >>>
# >>> %(s).3s: abc
# >>> %(s).4s: abcd
# >>> %(s).5s: abcde
# >>>
# >>> %(i).1i: 42
# >>> %(i).2i: 42
# >>> %(i).3i: 042
# >>> %(i).4i: 0042

# ## user `vars()` function with formatting to mimic string interpolation
foo = 42
bar = "BAR"
bat = [1, 2, 3]

template = """
foo: %(foo)i
bar: %(bar)s
bat: %(bat)r
"""

print(template % vars())

# >>> foo: 42
# >>> bar: BAR
# >>> bat: [1, 2, 3]

# >>> RESUME @ <<<
# ## advanced string formatting
