# Ask for user input with leading whitespaces
user_input = input("Input your full name: ")

# Remove spaces without using .lstrip()
while True:
    try:
        output = user_input.replace(" ", "")
        print(output)
    except ValueError:
        break