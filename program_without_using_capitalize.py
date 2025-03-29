# Ask for user input
user_input = input("Input your statement: ")

# Capitalize the first letter without using .capitalize()
# For loop to check each char
# Use ASCII code to convert lower to upper and vice versa
capitalize = ""
for char in user_input:
    if user_input[0] in "abcdefghijklmnopqrstuvwxyz":
        new_char = ord(user_input[0]) - 32
        capitalize += chr(new_char)
    elif user_input[1:] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        new_char = ord(user_input[1:]) + 32
        capitalize += new_char
    else:
        capitalize += char
print(capitalize)