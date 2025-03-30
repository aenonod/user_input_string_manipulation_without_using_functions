# Ask for user input
user_input = input("Input your statement: ")

# Convert text into uppercase without using .upper()
uppercase = ""
for char in user_input:     # For loop to check each char
    if "a" <= char <= "z":
        new_char = ord(char) - 32     # Use ASCII to convert lower to upper
        new_char += uppercase
    else:
        uppercase += char
print(uppercase)