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
