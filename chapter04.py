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

# >>> RESUME @ String Formatting <<<
