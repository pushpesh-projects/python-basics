"""
if(condition):
    Do something
else:
    Do something else
"""
print("----------Example 1--------------")
input_number = int(input("Enter a number"))
if input_number >= 100:
    print("You have entered a number greater than or equal to 100")
else:
    print("You have entered a number less than 100")

"""
if(condition 0):
    Do this if condition 0 is true
elif(condition 1):
    Do this if condition 1 is true
elif(condition 2):
    Do this if condition 2 is true
"""
print("----------Example 2--------------")
input_number = int(input("Enter a number"))
if 0 <= input_number < 100:
    print("You have entered a number between 0 too 100")
elif 100 <= input_number:
    print("You have entered a number greater than 100")


"""
If the condition for if is False, the program checks the conditions of the
subsequent elif blocks - the first elif block that is True is executed.
If all the conditions are False, the else block will be executed.

if(condition 0):
    Do this if condition 0 is true
elif(condition 1):
    Do this if condition 1 is true
elif(condition 2):
    Do this if condition 2 is true
else:
    Do this if none of the above conditions are true
"""

print("----------Example 3--------------")
input_number = int(input("Enter a number"))
if 0 <= input_number < 100:
    print("You have entered a number between 0 too 100")
elif 100 <= input_number:
    print("You have entered a number greater than 100")
else:
    print("You have entered a negative number")


# A series of if statements. Each if statement is tested separately.

print("----------Example 4--------------")
x = 10

if x > 5:  # condition one
    print("x is greater than 5")  # Executed if condition one is True.

if x < 10:  # condition two
    print("x is less than 10")  # Executed if condition two is True.

if x == 10:  # condition three
    print("x is equal to 10")  # Executed if condition three is True.

# a series of if statements followed by an else. Each if is tested separately.
# The body of else is executed if the last if is False.
print("----------Example 5--------------")
x = 10

if x > 5:  # True
    print("x > 5")

if x > 8:  # True
    print("x > 8")

if x > 10:  # False
    print("x > 10")

else:
    print("else will be executed")


"""
In Python, if number % 2 == 1: and if number % 2: are ways to write an if
statement that will execute a block of code if the value of number is odd.

The first version, if number % 2 == 1:, uses the modulo operator (%) to find
the remainder when number is divided by 2. If the remainder is equal to 1, it
means that number is odd. In this case, the block of code following the if
statement will be executed. If the remainder is not equal to 1, it means that
number is even, and the block of code will not be executed.

The second version, if number % 2:, also uses the modulo operator to find the
remainder when number is divided by 2. However, instead of explicitly checking
if the remainder is equal to 1, it relies on the fact that in Python, any value
that is considered "truthy" will be treated as True in a boolean context, and
any value that is considered "falsy" will be treated as False. The value 0 is
considered falsy, so if number is even, the result of number % 2 will be 0, and
the if statement will not execute the block of code. If number is odd, the
result of number % 2 will be 1, which is considered truthy, and the if
statement will execute the block of code.
"""

print("--------------Example 6----------------------")
number = 5

# Using if number % 2 == 1:
if number % 2 == 1:
    print("Number is odd")

# Output: Number is odd

number = 6

# Using if number % 2:
if number % 2:
    print("Number is odd")

# Output: (nothing)
