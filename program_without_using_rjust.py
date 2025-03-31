# Ask for user input
user_input = input("Input your statement: ")

# Ask for width of string
width = int(input("Input length of the string: "))

# Add spaces to fill specified width without using .rjust()
while len(user_input) < width:
    user_input = " " + user_input
print(user_input)