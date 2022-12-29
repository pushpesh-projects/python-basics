"""
Dictionaries are changeable (mutable), indexed collections of data.
In Python 3.6x dictionaries have become ordered by default.

If you want to access a dictionary item, you can do so by making a reference
to its key inside a pair of square brackets or by using the get() method.
"""
print("----------Example 1---------------")
# This way of creating a dictionary is called dictionary literal.
pol_eng_dictionary = {
    "kwiat": "flower",
    "woda": "water",
    "gleba": "soil"
    }

item_1 = pol_eng_dictionary["gleba"]    # ex. 1
print(item_1)    # outputs: soil

item_2 = pol_eng_dictionary.get("woda")
print(item_2)    # outputs: water

# If you want to change the value associated with a specific key,
# you can do so by referring to the item's key name in the following.

print("----------Example 2---------------")
pol_eng_dictionary = {"zamek": "lock", "woda": "water", "gleba": "soil"}
pol_eng_dictionary["zamek"] = "locker"
item = pol_eng_dictionary["zamek"]
print(item)  # outputs: locker

print("----------Example 3---------------")
# To add or remove a key (and the associated value), use the following syntax:
phonebook = {}    # an empty dictionary

phonebook["Adam"] = 3456783958    # create/add a key-value pair
print(phonebook)    # outputs: {'Adam': 3456783958}

del phonebook["Adam"]
print(phonebook)    # outputs: {}

# You can also insert an item to a dictionary by using the update() method,
# and remove the last element by using the popitem() method, e.g.:
print("----------Example 4---------------")
pol_eng_dictionary = {"kwiat": "flower"}

pol_eng_dictionary.update({"gleba": "soil"})
print(pol_eng_dictionary)    # outputs: {'kwiat': 'flower', 'gleba': 'soil'}

pol_eng_dictionary.popitem()
print(pol_eng_dictionary)    # outputs: {'kwiat': 'flower'}

# You can use the for loop to loop through a dictionary, e.g.:
print("----------Example 5---------------")
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

for item in pol_eng_dictionary:
    print(item)

# outputs: zamek
#          woda
#          gleba


# If you want to loop through a dictionary's keys and values,
# you can use the items() method, e.g.:
print("----------Example 6---------------")
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

for key, value in pol_eng_dictionary.items():
    print("Pol/Eng ->", key, ":", value)

# To check if a given key exists in a dictionary, you can use the in keyword:
print("----------Example 7---------------")
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

if "zamek" in pol_eng_dictionary:
    print("Yes")
else:
    print("No")

# You can use the del keyword to remove a specific item, or delete a dictionary
# To remove all the dictionary's items, you need to use the clear() method.
print("----------Example 8---------------")
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

print(len(pol_eng_dictionary))    # outputs: 3
del pol_eng_dictionary["zamek"]    # remove an item
print(len(pol_eng_dictionary))    # outputs: 2

pol_eng_dictionary.clear()   # removes all the items
print(len(pol_eng_dictionary))    # outputs: 0

del pol_eng_dictionary    # removes the dictionary

print("----------Example 9---------------")
# To copy a dictionary, use the copy() method:
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

copy_dictionary = pol_eng_dictionary.copy()
print(copy_dictionary)

print("----------Example 10---------------")
# Write a program that will convert the colors tuple to a dictionary.
colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors)
print(colors_dictionary)

print("----------Example 11---------------")
#  Write a program that will "glue" the two dictionaries (d1 and d2)
#  together and create a new one (d3).
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)
