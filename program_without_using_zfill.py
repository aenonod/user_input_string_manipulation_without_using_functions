# Ask for user input
user_input = input("Input text/number: ")

# Ask for width of string
width = int(input("Input length of the string: "))

# Add zeros in front of the user_input without using .zfill()
while len(user_input) < width:
    user_input = "0" + user_input
print(user_input)