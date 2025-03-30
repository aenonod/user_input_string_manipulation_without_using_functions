# Ask for user 
user_input = input("Input your statement: ")

# Ask what to remove from the input
suffix_to_remove = input("What do you want to remove from the statement: ")

# Remove suffix without using .removesuffix()
if user_input.endswith(suffix_to_remove):
    output = user_input.replace(suffix_to_remove,"")
    print(output)
else:
    print(user_input)