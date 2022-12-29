"""
The while loop executes a statement or a set of statements as long as a
specified boolean condition is true.
# Example 1
while True:
    print("Stuck in an infinite loop.")

# Example 2
counter = 5
while counter > 2:
    print(counter)
    counter -= 1
"""
print("--------------Example 1----------------------")
number = 5

# Using while number != 0:
while number != 0:
    print(number)
    number -= 1

# Output: 5 4 3 2 1

number = 5

# Using while number:
while number:
    print(number)
    number -= 1

# Output: 5 4 3 2 1

"""
In Python, both while number != 0: and while number: are ways to write a while
loop that will continue to execute as long as the value of number != 0.

The first version, while number != 0:, checks if number is not equal to 0.
If number is not equal to 0, the loop will execute. If number is equal to 0,
the loop will terminate.

The second version, while number:, takes advantage of the fact that in Python,
any value that is considered "truthy" will be treated as True in a boolean
context, and any value that is considered "falsy" will be treated as False.
The values 0 and None are considered falsy, so if number is either of these
values, the loop will terminate. Otherwise, the loop will execute.
"""

"""
loops may have the else branch too, like ifs.
The loop's else branch is always executed once, regardless of whether the loop
has entered its body or not.
"""
print("--------------Example 2----------------------")
# Here loop will be executed and then the else statement
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

print("--------------Example 3----------------------")
# Here the loop will not be executed but else will be executed
i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)
