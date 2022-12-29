"""
The for loop executes a set of statements many times; it's used to iterate
over a sequence (e.g., a list, a dictionary, a tuple, or a set or other objects
that are iterable (e.g., strings). You can use the for loop to iterate over a
sequence of numbers using the built-in range function.

# Example 1
word = "Python"
for letter in word:
    print(letter, end="*")

# Example 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)

The range() function generates a sequence of numbers. It accepts integers
and returns range objects. The syntax of range() looks as follows:
range(start, stop, step), where:
start is an optional parameter specifying the starting number of the sequence
(0 by default)
stop is an optional parameter specifying the end of the sequence generated
(it is not included),
and step is an optional parameter specifying the difference between the numbers
in the sequence (1 by default.)

for i in range(100):
    # do_something()
    pass

The value of i starts from 0 and maximum value goes till 99.
Note: pass keyword inside the loop body - it does nothing at all; it's an empty
instruction - we put it here because the for loop's syntax demands at least one
instruction inside the body (by the way - if, elif, else and while express the
same thing)

The range() function invocation may be equipped with two arguments.

The range() function may also accept three arguments.

The third argument is an increment - it's a value added to control the variable
at every loop turn , the default value of the increment is 1).

for i in range(3):
    print(i, end=" ")  # Outputs: 0 1 2

for i in range(6, 1, -2):
    print(i, end=" ")  # Outputs: 6, 4, 2
"""
print("-----------Example 1--------------")
# The value of i starts from 0 and maximum value goes till 4.

for i in range(5):
    print("The value of i is currently", i)

print("-----------Example 2--------------")
# The value of i starts from 2 and maximum value goes till 7.

for i in range(2, 8):
    print("The value of i is currently", i)

print("-----------Example 3--------------")
# The value of i starts from 2, increments by 3 and goes till 7

for i in range(2, 8, 3):
    print("The value of i is currently", i)

"""
loops may have the else branch too, like ifs.
The loop's else branch is always executed once, regardless of whether the loop
has entered its body or not.
"""
print("-----------Example 4--------------")
for i in range(5):
    print(i)
else:
    print("else:", i)

print("-----------Example 5--------------")

i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)

"""
Note: if the set generated by the range() function is empty, the loop won't
execute its body at all.

Note: the set generated by the range() has to be sorted in ascending order.
There's no way to force the range() to create a set in a different form when
the range() function accepts exactly two arguments. This means that the
range()'s second argument must be greater than the first.

"""
print("-----------Example 6--------------")
# No output
for i in range(1, 1):
    print("The value of i is currently", i)

print("-----------Example 7--------------")
# No output
for i in range(2, 1):
    print("The value of i is currently", i)
