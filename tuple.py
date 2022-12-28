"""
Tuples prefer to use parenthesis, whereas lists like to see brackets,
although it's also possible to create a tuple just from a set of values
separated by commas.

It is possible to create an empty tuple - parentheses are required then:
empty_tuple = ()

If you want to create a one-element tuple, you must end the value with a comma.

Tuples are ordered and unchangeable (immutable) collections of data.
They can be thought of as immutable lists.
"""
print("----------Example 1---------------")
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

print(tuple_1)  # (1, 2, 4, 8)
print(tuple_2)  # (1.0, 0.5, 0.25, 0.125)

print("----------Example 2---------------")
one_element_tuple_1 = (1, )
one_element_tuple_2 = 1.,
print(one_element_tuple_1, one_element_tuple_2)

print("----------Example 3---------------")
my_tuple = (1, 2, True, "a string", (3, 4), [5, 6], None)
print(my_tuple)

my_list = [1, 2, True, "a string", (3, 4), [5, 6], None]
print(my_list)

print("----------Example 4---------------")
empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))    # outputs: <class 'tuple'>

print("----------Example 5---------------")
# Some operations on tuples
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])  # 1
print(my_tuple[-1])  # 1000
print(my_tuple[1:])  # (10, 100, 1000)
print(my_tuple[:-2])  # (1, 10)

for elem in my_tuple:
    print(elem)

print("----------Example 6---------------")
# Trying to modify the tuple cause run time error
# AttributeError: 'tuple' object has no attribute 'append'
# my_tuple.append(10000)
# del my_tuple[0]
# my_tuple[1] = -10

print("----------Example 7---------------")
my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))  # 9
print(t1)  # (1, 10, 100, 1000, 10000)
print(t2)  # (1, 10, 100, 1, 10, 100, 1, 10, 100)
print(10 in my_tuple)  # True
print(-10 not in my_tuple)  # True

print("----------Example 8---------------")
# A tuple's elements can be variables, not only literals.
# Moreover, they can be expressions if they're on the right side of
# the assignment operator.

var = 123

t1 = (1, )  # Single element tuple
t2 = (2, )  # Single element tuple
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)  # (2,) (3, 123) (1,)

print("----------Example 9---------------")
# However, you can delete a tuple as a whole:
my_tuple = 1, 2, 3,  # (1, 2, 3)
print(my_tuple)
del my_tuple
# print(my_tuple)    # NameError: name 'my_tuple' is not defined

# You can also create a tuple using a Python built-in function called tuple().
# This is particularly useful when you want to convert a certain iterable
# (e.g., a list, range, string, etc.) to a tuple:
print("----------Example 10---------------")
my_tuple = tuple((1, 2, "string"))
print(my_tuple)  # (1, 2, 'string')

my_list = [2, 4, 6]
print(my_list)  # outputs: [2, 4, 6]
print(type(my_list))  # outputs: <class 'list'>
tup = tuple(my_list)
print(tup)    # outputs: (2, 4, 6)
print(type(tup))    # outputs: <class 'tuple'>

print("----------Example 11---------------")
# By the same fashion, when you want to convert an iterable to a list,
# you can use a Python built-in function called list():
tup = 1, 2, 3,
my_list = list(tup)
print(my_list)
print(type(my_list))    # outputs: <class 'list'>

print("----------Example 12---------------")
# Complete the code to correctly use the count() method to find the number
# of duplicates
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)
print(duplicates)    # outputs: 4
