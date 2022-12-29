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
