# Ask for user input with leading whitespaces
user_input = input("Input your full name: ")

# Remove spaces without using .lstrip()
while user_input and user_input[0] == ' ':
    output = user_input[1:]
    print(output)