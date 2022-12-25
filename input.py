"""
The result of the input() function is a string.
A string containing all the characters the user enters from the keyboard.
It is not an integer or a float.
the int() function takes one argument (e.g., a string: int(string)) and tries to convert it into an integer;
the float() function takes one argument (e.g., a string: float(string)) and tries to convert it into a float.
str() function takes one argument and tries to convert it to string
"""

num = input("Enter the number: ")
square = int(num) ** 2
print("Square of the number is: " + str(square))
# In the below line we don't type cast integer to string because we are not concatinating the string to integer.
# print function can take different types of literals separated by comma.
print("Square of the number is:", square)


#  You can also multiply (* - replication) strings, e.g.:
my_input = input("Enter something: ")  # Example input: hello
print(my_input * 3)  # Expected output: hellohellohello
