# Ask for user input
user_input = input("Input your statement: ")

# Swap casing without using .swapcase()
swapped = ""
for char in user_input:     # For loop to check each char
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        new_char = ord(char) + 32     # Use ASCII code for upper to lower
        swapped += chr(new_char)
    elif char in "abcdefghijklmnopqrstuvwxyz":
        new_char = ord(char) - 32     # Use ASCII code for lower to upper
        swapped += chr(new_char)
    else:
        swapped += char
print(swapped)