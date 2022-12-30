"""
Arithmetic operators: exponentiation
A ** (double asterisk) sign is an exponentiation (power) operator.
Its left argument is the base, its right, the exponent.
When both ** arguments are integers, the result is an integer and when at
least one ** argument is a float, the result is a float.
"""
print("----------Example 1--------------")
print(2 ** 3)  # 8
print(2 ** 3.)  # 8.0
print(2. ** 3)  # 8.0
print(2. ** 3.)  # 8.0

# An * (asterisk) sign is a multiplication operator. When both ** arguments are
# integers, the result is an integer and when at
# least one ** argument is a float, the result is a float.
print("----------Example 2--------------")
print(2 * 3)  # 6
print(2 * 3.)  # 6.0
print(2. * 3)  # 6.0
print(2. * 3.)  # 6.0

# A / (slash) sign is a divisional operator.
# The value in front of the slash is a dividend, the value behind the slash,
# a divisor.The result produced by the division operator is always a float.
print("----------Example 3--------------")
print(6 / 3)  # 2.0
print(6 / 3.)  # 2.0
print(6. / 3)  # 2.0
print(6. / 3.)  # 2.0

# A + sign is a addition operator. When both + arguments are
# integers, the result is an integer and when at
# least one + argument is a float, the result is a float.
print("----------Example 4--------------")
print(6 + 3)  # 9
print(6 + 3.)  # 9.0
print(6. + 3)  # 9.0
print(6. + 3.)  # 9.0

# A // (double slash) sign is an integer divisional operator. It differs from
# the standard / operator in two details:
# its result lacks the fractional part - it's absent (for integers),
# or is always equal to zero (for floats). this means that the results are
# always rounded to the nearest integer value that is less than the real
# result.
# It conforms to the integer vs. float rule.
print("----------Example 5--------------")
print(6 // 3)  # 2
print(6 // 3.)  # 2.0
print(6. // 3)  # 2.0
print(6. // 3.)  # 2.0

print(6 // 4)  # 1
print(6. // 4)  # 1.0

print(-6 // 4)  # -2
print(6. // -4)  # -2.0

# The result is two negative twos. The real (not rounded) result is -1.5 in
# both cases.However, the results are the subjects of rounding.
# The rounding goes toward the lesser integer value, and the lesser integer
# value is -2, hence: -2 and -2.0.

# remainder (modulo)
# The result of the operator is a remainder left after the integer division.
print("----------Example 6--------------")
print(14 % 4)  # 2
print(12 % 4.5)  # 3.0

"""
Do not try to:
perform a division by zero;
perform an integer division by zero;
find a remainder of a division by zero.
"""

"""
PEMDAS : Parenthesis exponentiation multiplication division addition
subtraction
Priority	Operator
1	**
2	+, - (note: unary operators located next to the right of the power operator
bind more strongly)	unary
3	*, /, //, %
4	+, -	binary

the exponentiation operator uses right-sided binding.
Most of Python's operators have left-sided binding, which means that the
calculation of the expression is conducted from left toright.
"""
print("----------Example 7--------------")
print(2 ** 2 ** 3)  # Right sided binding 256
print(9 % 6 % 2)  # Left sided binding 1

"""
Comparison: equality operator
Question: are two values equal?
To ask this question, you use the == (equal equal) operator.
Don't forget this important distinction:
= is an assignment operator, e.g., a = b assigns a with the value of b;
== is the question are these values equal?; a == b compares a and b.
It is a binary operator with left-sided binding.
It needs two arguments and checks if they are equal.

2 == 2 True
2 == 2.0 True
1 == 2 False

Inequality: the not equal to operator (!=)
The != (not equal to) operator compares the values of two operands, too.
Here is the difference: if they are equal, the result of the comparison is
False. If they are not equal, the result of the comparison is True.

Comparison operators: greater than
You can also ask a comparison question using the > (greater than) operator.
True confirms it; False denies it.

Comparison operators: greater than or equal to
Comparison operators: less than or equal to
Their priority is greater than that shown by == and !=
Priority	Operator
1	+, -	unary
2	**
3	*, /, //, %
4	+, -	binary
5	<, <=, >, >=
6	==, !=
"""

"""
Python supports the following logical operators:

and → if both operands are true, the condition is true,(True and True) is True.
or → if any of the operands are true, the condition is true, e.g.,
(True or False) is True,
not → returns false if the result is true, and returns true if the result is
false, e.g., not True is False.
"""

"""
You can use bitwise operators to manipulate single bits of data.
The following sample data:

x = 15, which is 0000 1111 in binary,
y = 16, which is 0001 0000 in binary.
will be used to illustrate the meaning of bitwise operators in Python.
Analyze the examples below.

& does a bitwise and, e.g., x & y = 0, which is 0000 0000 in binary,
| does a bitwise or, e.g., x | y = 31, which is 0001 1111 in binary,
˜  does a bitwise not, e.g., ˜ x = 240*, which is 1111 0000 in binary,
^ does a bitwise xor, e.g., x ^ y = 31, which is 0001 1111 in binary,
>> does a bitwise right shift, e.g., y >> 1 = 8, which is 0000 1000 in binary,
<< does a bitwise left shift, e.g., y << 3 = , which is 1000 0000 in binary,
"""


"""
here is the updated priority table, containing all the operators:

Priority	Operator
1	~, +, -	unary
2	**
3	*, /, //, %
4	+, -	binary
5	<<, >>
6	<, <=, >, >=
7	==, !=
8	&
9	|
10	=, +=, -=, *=, /=, %=, &=, ^=, |=, >>=, <<=
"""
