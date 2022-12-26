print("The itsy bitsy spider climbed up the waterspout.")
print()  # prints an empty line
print("Down came the rain and washed the spider out.")

"""
The backslash (\) has a very special meaning when used inside strings - this is called the escape character.
The letter n placed after the backslash comes from the word newline.
Both the backslash and the n form a special symbol named a newline character, which urges the console to start 
a new output line.

This convention has two important consequences:
1. If you want to put just one backslash inside a string, don't forget its escaping nature - you have to double it, 
e.g., such an invocation will cause a syntax error:
print("\")
while this one won't:
print("\\")
"""
print("The itsy bitsy spider\nclimbed up the waterspout.")
print()
print("Down came the rain\nand washed the spider out.")
print("\\")

"""
The print() function - using multiple arguments
a print() function invoked with more than one argument outputs them all on one line;
the print() function puts a space between the outputted arguments on its own initiative.
"""
print("The itsy bitsy spider", "climbed up", "the waterspout.")

"""
Positional arguments are the ones whose meaning is dictated by their position, e.g., the second argument is outputted 
after the first, the third is outputted after the second, etc.
Keyword arguments are the ones whose meaning is not dictated by their location, 
but by a special word (keyword) used to identify them.
The end and sep parameters can be used for formatting the output of the print() function. 
The sep parameter specifies the separator between the outputted arguments (e.g., print("H", "E", "L", "L", "O", sep="-")
, whereas the end parameter specifies what to print at the end of the print statement.
"""
print("Programming", "Essentials", "in", sep="***", end="...")
print("Python")
# output = Programming***Essentials***in...Python
print("Programming", "Essentials", "in", end="")
print("Python")
# output = Programming Essentials inPython
print("Programming", "Essentials", "in", end=" ")
print("Python")
# output = Programming Essentials in Python
print('"I\'m"\n""learning""\n"""Python"""')
# above line prints
# "I'm"
# ""learning""
# """Python"""

"""
Literals
Literals are notations for representing some fixed values in code. Python has various types of literals - for example, 
a literal can be a number (numeric literals, e.g., 123), or a string (string literals, e.g., "I am a literal.").
There is one more, special literal that is used in Python: the None literal. 
This literal is a so-called NoneType object, and it is used to represent the absence of a value. 
Boolean values are the two constant objects True and False used to represent truth values 
(in numeric contexts 1 is True, while 0 is False.
see examples of literals below
"""
print(None)
print(True)
print(False)
print(2)
print(2.5)

# Data and operators when connected together form expressions. The simplest expression is a literal itself.
print(2 + 2)  # 4

print(1 + 2939)  # 2940
print(2940 % 60)  # 0
print(2940 // 60)  # 49
print(49 % 24)  # 1
