# Ask for user input
user_input = input("Input your statement: ")

# Convert text into lowercase without using .lower()
lowercase = ""
for char in user_input:     # For loop to check each char
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        new_char = ord(char) + 32     # Use ASCII to convert upper to lower
        lowercase += chr(new_char)
    else:
        lowercase += char
print(lowercase)