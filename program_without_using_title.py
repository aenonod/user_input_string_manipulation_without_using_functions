# Ask for user input
user_input = input("Input your statement: ")

# Convert text to title casing without using .title()
# Split input by words
titled = ""
for word in user_input.split():
    if "a" <= word[0] <= "z":
        new_charac = ord(word[0]) - 32
        titled += chr(new_charac)
    else:
        titled += word
        
    succeeding_letters = word[1:].lower()
    titled += succeeding_letters + " "
print(titled)