# Ask for user input
user_input = input("Input your statement: ")

# Ask if the user_input ends with the given word
suffix = input("Input the suffix to check: ")

# Check if it ends with the given word without using .endswith()
len_of_suffix = len(suffix)
from_string = user_input[-(len_of_suffix):]

if suffix == from_string:
    print(True)
else:
    print(False)