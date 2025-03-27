# Ask for user input
user_input = input("Input your statement: ")

# Ask what to remove from the input
to_remove = input("What do you want to remove from the statement: ")

# Remove prefix without using .removeprefix()
output = user_input.replace(to_remove,"")
print(output)