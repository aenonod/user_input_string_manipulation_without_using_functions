# Ask for user input
user_input = input("Input your statement: ")

# Capitalize the first letter without using .capitalize()
# Use ASCII code to convert lower to upper and vice versa
capitalize = ""
if "a" <= user_input[0] <= "z":
    new_char = ord(user_input[0]) - 32
    capitalize += chr(new_char)
else:
    capitalize += user_input[0]

for char in user_input[1:]:     # For loop to check each char
    if "A" <= char <= "Z":
        new_char = ord(char) + 32
        capitalize += chr(new_char)
    else:
        capitalize += char
print(capitalize)