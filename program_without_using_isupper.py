# Ask for user input
user_input = input("Input your statement: ")

# Check is user input is uppercase without using .isupper()
output = ""
for char in user_input:     # Use for loop to check each char
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        output = True
    else:
        output = False
print(output)