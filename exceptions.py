# You can handle multiple exceptions in your code block.
while True:
    try:
        number = int(input("Enter an int number: "))
        print(5 / number)
        break
    except ValueError:
        print("Wrong value.")
    except ZeroDivisionError:
        print("Sorry. I cannot divide by zero.")
    except:
        print("I don't know what to do...")

#  You can use multiple except blocks within one try statement,
#  and specify particular exception names.
#  If one of the except branches is executed, the other branches will be
#  skipped.
#  Remember: you can specify a particular built-in exception only once.
#  Also, don't forget that the default (or generic) exception,
#  that is the one with no name specified, should be placed at the bottom of
#  the branch(use the more specific exceptions first,
#  and the more general last).

while True:
    try:
        number = int(input("Enter an int number: "))
        print(5 / number)
        break
    except (ValueError, ZeroDivisionError):
        print("Wrong value or No division by zero rule broken.")
    except:
        print("Sorry, something went wrong...")

"""
Most common exceptions in python.

ZeroDivisionError
This appears when you try to force Python to perform any operation which
provokes division in which the divider is zero.
Python operator which may cause this exception to raise: /, //, and %.

ValueError
It is a built-in Python exception that is raised when a built-in operation or
function receives an argument that has the right type but an inappropriate
value. For example, you might see a ValueError if you try to convert a
string to an integer and the string can't be parsed as a valid integer.
Here is an example of how a ValueError could be raised in Python:
x = int("hello")
This would raise a ValueError because the string "hello" cannot be converted
to an integer.

TypeError
This exception shows up when you try to apply a data whose type cannot be
accepted in the current context. Look at the example:
short_list = [1]
one_value = short_list[0.5]
You're not allowed to use a float value as a list index
(the same rule applies to tuples, too).

AttributeError
This exception arrives – among other occasions – when you try to activate a
method which doesn't exist in an item you're dealing with. For example:

short_list = [1]
short_list.append(2)
short_list.depend(3)

SyntaxError
This exception is raised when the control reaches a line of code which violates
Python's grammar. It may sound strange, but some errors of this kind cannot be
identified without first running the code. This kind of behavior is typical
of interpreted languages – the interpreter always works in a hurry and has no
time to scan the whole source code.
"""
