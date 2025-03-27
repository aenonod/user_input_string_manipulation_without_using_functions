# Ask for user input
user_input = input("Input your statement: ")

# Ask what to remove from the input
prefix_to_remove = input("What do you want to remove from the statement: ")

# Remove prefix without using .removeprefix()
if user_input.startswith(prefix_to_remove):
    output = user_input.replace(prefix_to_remove,"")
    print(output)
else:
    print(user_input)