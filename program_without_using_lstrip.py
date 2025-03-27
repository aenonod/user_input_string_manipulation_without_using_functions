# Ask for user input with leading whitespaces
user_input = input("Input your full name: ")

# Remove spaces without using .lstrip()
output = user_input
while output and output[0] == ' ':
    output = output[1:]
    print(output)