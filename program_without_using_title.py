# Ask for user input
user_input = input("Input your statement: ")

# Convert text to title casing without using .title()
# Split input by words
titled = ""
for word in user_input.split():
    if word[0] in "abcdefghijklmnopqrstuvwxyz":
        new_charac = ord(word[0]) - 32
        titled += chr(new_charac)