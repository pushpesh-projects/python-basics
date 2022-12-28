"""
You mustn't invoke a function which is not known at the moment of invocation.

if we try to run this, it will give NameError message is not defined.
print("We start here.")
message()
print("We end here.")
def message():
    print("Enter a value: ")

You mustn't have a function and a variable of the same name.
The following snippet is erroneous:
def message():
    print("Enter a value: ")
message = 1

Assigning a value to the name message causes Python to forget its previous role
The function named message becomes unavailable.
"""

"""
Positional parameter passing
A technique which assigns the ith (first, second, and so on) argument to the
ith (first, second, and so on)function parameter is called positional parameter
passing, while arguments passed in this way are named positional arguments.

Keyword argument passing
Python offers another convention for passing arguments, where the meaning of
the argument is dictated by its name,not by its position-it's called keyword
argument passing.

keyword (named) argument passing in which the order of arguments passed doesn't
matter.

def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")

Mixing positional and keyword arguments
You can mix both fashions if you want - there is only one unbreakable rule:
you have to put positional arguments before keyword arguments.
positional arguments mustn't follow keyword arguments. It causes SyntaxError.

If you try to pass more than one value to one argument,
all you'll get is a runtime error.

It happens at times that a particular parameter's values are in use more often
than others.Such arguments may have their default (predefined) values taken
into consideration when their corresponding arguments have been omitted.

def introduction(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

introduction("Henry")  # Hello, my name is Henry Smith

introduction(first_name="William")  # Hello, my name is William Smith
"""

"""
return keyword can have expressions.
return keyword can be used without expression as well.
Note: if a function is not intended to produce a result,
using the return instruction is not obligatory - it will be executed implicitly
at the end of the function.you can use it to terminate a function's activities
on demand, before the control reaches the function's last line.

you are always allowed to ignore the function's result,
and be satisfied with the function's effect (if the function has any)
The below does not cause any error:

def boring_function():
    print("'Boredom Mode' ON.")
    return 123

print("This lesson is interesting!")
boring_function()
print("This lesson is boring...")

Output:
This lesson is interesting!
'Boredom Mode' ON.
This lesson is boring...
"""

"""
None keyword
Its data doesn't represent any reasonable value - actually, it's not a value at
all; hence, it mustn't take part in any expressions.
print(None + 2) will cause a runtime error:
TypeError: unsupported operand type(s) for +

There are only two kinds of circumstances when None can be safely used:

when you assign it to a variable (or return it as a function's result)
when you compare it with a variable to diagnose its internal state.

Don't forget this: if a function doesn't return a certain value using a return
expression clause,it is assumed that it implicitly returns None.

The return statement exits the function
"""
print("----------Example 1---------------")
value = None
if value is None:
    print("Sorry, you don't carry any value")

print("----------Example 2---------------")


def hello():
    print("I will try to return none")


print(hello())  # None

print("----------Example 3---------------")


def i_exit_before_printing_due_to_return_keyword():
    return
    print("I can do something")


i_exit_before_printing_due_to_return_keyword()

print("----------Example 4---------------")


# Leap year calculator


def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

print("----------Example 5---------------")


def days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        check_year = is_year_leap(year)
        if check_year is True:
            return 29
        else:
            return 28


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

# Your task is to write and test a function which takes three arguments
# (a year, a month, and a day of the month)
# and returns the corresponding day of the year, or returns None if any of
# the arguments is invalid
print("----------Example 6---------------")


def day_of_year(year, month, day):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check if year is a leap year
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                days_in_month[1] = 29
        else:
            days_in_month[1] = 29

    # Check if month and day are valid
    if month < 1 or month > 12:
        return None
    if day < 1 or day > days_in_month[month - 1]:
        return None

    # Calculate day of year
    day_of_year = day
    for i in range(month - 1):
        day_of_year += days_in_month[i]

    return day_of_year


print(day_of_year(2000, 12, 31))
print(day_of_year(2001, 12, 31))
print(day_of_year(2000, 3, 1))

print("----------Example 7---------------")


# Prime number :


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")

# A variable that exists outside a function has a scope inside the function
# body unless the function defines a variable of the same name.
print("\n----------Example 8---------------")
var = 2


def mult_by_var(x):
    return x * var


print(mult_by_var(7))  # outputs: 14

# Variable shadowing occurs when a variable defined in the inner scope
# has the same name as a variable in the outer scope.
# Python treats these variables as completely separate variables.
# The global variable a is said to be shadowed by the local variable a.
print("----------Example 9---------------")


def mult(x):
    var = 7
    return x * var


var = 3
print(mult(7))  # outputs: 49

# A variable that exists inside a function has a scope inside the function body
print("----------Example 10---------------")


def adding(x):
    var = 7
    return x + var


print(adding(4))  # outputs: 11
# print(var)    # NameError

print("----------Example 11---------------")
# You can use the global keyword followed by a variable name to make the
# variable's scope global, e.g.:
var = 2
print(var)  # outputs: 2


def return_var():
    global var
    var = 5
    return var


print(return_var())  # outputs: 5
print(var)  # outputs: 5

print("----------Example 12---------------")


# factorial number


def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1

    product = 1
    for i in range(2, n + 1):
        product *= i
    return product


for n in range(1, 6):  # testing
    print(n, factorial_function(n))

print("----------Example 13---------------")


#  Fibonacci numbers:


def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):  # testing
    print(n, "->", fib(n))

# factorial using recursion
# Recursive implementation of the factorial function.
print("----------Example 14---------------")


def factorial(n):
    if n == 1:  # The base case (termination condition.)
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4))  # 4 * 3 * 2 * 1 = 24
print("----------Example 15---------------")


# A list can be sent to a function as an argument.
def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s


print(list_sum([5, 4, 3]))
print("----------Example 16---------------")


# a list can be a function result as well.


def strange_list_fun(n):
    strange_list = []

    for i in range(0, n):
        strange_list.insert(0, i)

    return strange_list


print(strange_list_fun(5))
print("----------Example 17---------------")


# How the function interacts with its arguments
# changing the parameter's value doesn't propagate outside the function


def my_function(n):
    print("I got", n)
    n += 1
    print("I have", n)


var = 1
my_function(var)
print(var)
print("----------Example 17---------------")


def my_function(my_list_1):
    # Here my_list_1 and my_list_2 refers to the same list [2, 3]
    print("Print #1:", my_list_1)
    # Here my_list_1 and my_list_2 refers to the same list [2, 3]
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]  # Now my_list_1 refers to a new list
    print("Print #3:", my_list_1)  # [0, 1]
    print("Print #4:", my_list_2)  # [2, 3]


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)  # [2, 3]
print("----------Example 18---------------")


def my_function(my_list_1):
    # Here my_list_1 and my_list_2 refers to the same list [2, 3]
    print("Print #1:", my_list_1)
    # Here my_list_1 and my_list_2 refers to the same list [2, 3]
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Here we deleted the index 0 of list [2, 3]
    print("Print #3:", my_list_1)  # [3]
    print("Print #4:", my_list_2)  # [3]


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)  # [3]
