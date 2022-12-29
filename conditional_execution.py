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
