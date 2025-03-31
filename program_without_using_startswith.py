# Ask for user input
user_input = input("Input your statement: ")

# Ask if the user_input starts with the given word
prefix = input("Input the prefix to check: ")

# Check if it starts with the given word without using .startswith()
len_of_prefix = len(prefix)
from_string = user_input[:(len_of_prefix)]
                         
if prefix == from_string:
    print(True)
else:
    print(False)