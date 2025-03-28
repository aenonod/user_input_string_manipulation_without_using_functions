# Ask user input
user_input = input("Input your statement: ")

# Ask for width of string
width = int(input("Input length of the string: "))

# Add spaces to fill specified width without using .ljust()
while True:
    len_str = len(user_input))

    if len_str < width:
        user_input += " "
    else:
        break
print(user_input)