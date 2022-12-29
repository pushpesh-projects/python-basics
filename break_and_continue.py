"""
break - exits the loop immediately, and unconditionally ends the loop's
operation; the program begins to execute the nearest instruction after the
loop's body;

continue - behaves as if the program has suddenly reached the end of the body;
the next turn is started and the condition expression is tested immediately.
"""

print("---------------Example 1------------------")
# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

print("---------------Example 2------------------")
word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input()
user_word = user_word.upper()
for letter in user_word:
    # Complete the body of the for loop.
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    if letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else:
        word_without_vowels = word_without_vowels + letter

print(word_without_vowels)
