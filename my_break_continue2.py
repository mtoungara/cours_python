# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("Enter Word: ")

for letter in user_word.upper():
# Complete the body of the for loop.
    if letter in ('A','E','I','O','U'):
        continue
print(letter)