"""
The list is a type of data in Python used to store multiple objects. It is an
ordered and mutable collection of comma-separated items between square brackets
"""
print("----------Example 1-----------")
my_list = [1, None, True, "I am a string", 256, 0]
print(my_list)

print("----------Example 2-----------")
# Lists can be indexed and updated. Index starts from 0. -1 refers to the
# last index.
my_list = [1, None, True, 'I am a string', 256, 0]
print(my_list[3])  # outputs: I am a string
print(my_list[-1])  # outputs: 0

print("----------Example 3-----------")
my_list[1] = '?'
print(my_list)  # outputs: [1, '?', True, 'I am a string', 256, 0]

print("----------Example 4-----------")
my_list.insert(0, "first")  # insert at the specified index position
my_list.append("last")  # insert at the last index position
print(my_list)
# outputs: ['first', 1, '?', True, 'I am a string', 256, 0, 'last']

print("----------Example 5-----------")
# Lists can be nested, e.g.:
my_list = [1, 'a', ["list", 64, [0, 1], False]]
print(my_list)

print("----------Example 6-----------")
# List elements and lists can be deleted
my_list = [1, 2, 3, 4]
del my_list[2]
print(my_list)  # outputs: [1, 2, 4]

del my_list  # deletes the whole list

print("----------Example 7-----------")
# Lists can be iterated through using the for loop, e.g.
my_list = ["white", "purple", "blue", "yellow", "green"]

for color in my_list:
    print(color)

print("----------Example 8-----------")
# The len() function may be used to check the list's length
my_list = ["white", "purple", "blue", "yellow", "green"]
print(len(my_list))  # outputs 5

del my_list[2]
print(len(my_list))  # outputs 4

print("----------Example 9-----------")
# If you want Python to sort your list, you can do it like this:
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

print("----------Example 10-----------")
# There is also a list method called reverse(), which you can use to reverse
# the list, e.g.:
lst = [5, 3, 1, 2, 4]
print(lst)
lst.reverse()
print(lst)  # outputs: [4, 2, 1, 3, 5]

print("----------Example 11-----------")
list_1 = [1]
list_2 = list_1  # Both list_2 and list_1 refers to the same list [1]
list_1[0] = 2
print(list_2)

print("----------Example 12-----------")
# If you want to copy a list or part of the list, you can do it by
# performing slicing. slicing creates a brand new list.
colors = ['red', 'green', 'orange']

copy_whole_colors = colors[:]  # start index = 0, end index = len(list) -1
# copy part of the list. start index = 0, end index = 2-1 = 1
copy_part_colors = colors[0:2]  # copy part of the list

print("----------Example 13-----------")
# You can use negative indices to perform slices, too
sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)  # outputs: ['C', 'D']

# The start and end parameters are optional when performing a slice
print("----------Example 14-----------")
my_list = [1, 2, 3, 4, 5]
slice_one = my_list[2:]
slice_two = my_list[:2]
slice_three = my_list[-2:]

print(slice_one)  # outputs: [3, 4, 5]
print(slice_two)  # outputs: [1, 2]
print(slice_three)  # outputs: [4, 5]

print("----------Example 15-----------")
# You can delete slices using the del instruction.
my_list = [1, 2, 3, 4, 5]
del my_list[0:2]
print(my_list)  # outputs: [3, 4, 5]

del my_list[:]
print(my_list)  # deletes the list content, outputs: []

del my_list  # This deleted the list itself

print("----------Example 16-----------")
#  You can test if some items exist in a list or not using the keywords
#  in and not in
my_list = ["A", "B", 1, 2]

print("A" in my_list)  # outputs: True
print("C" not in my_list)  # outputs: True
print(2 not in my_list)  # outputs: False


# List comprehension allows you to create new lists from existing ones in a
# concise and elegant way. The syntax of a list comprehension looks as follows:
# [expression for element in list if conditional]

print("----------Example 17-----------")
# the code creates a five-element list filled with with the first five natural
# numbers raised to the power of 3
cubed = [num ** 3 for num in range(5)]
print(cubed)  # outputs: [0, 1, 8, 27, 64]
twos = [2 ** i for i in range(8)]
print(twos)

squares = [2, 3, 4, 5, 6, 7]
odds = [x for x in squares if x % 2 != 0]
print(odds)

print("----------Example 18-----------")
# swapping
variable_1 = 1
variable_2 = 2
print("Before swapping", variable_1, variable_2)

variable_1, variable_2 = variable_2, variable_1
print("After swapping", variable_1, variable_2)


print("----------Example 19-----------")
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

list_1, list_2 = list_2, list_1

print(list_1, list_2)
