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

# >>> RESUME @ <<<<
# ## Operations on Sequences
