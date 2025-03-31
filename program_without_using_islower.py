# Ask for user input
user_input = input("Input your statement: ")

# Check if user input is lowercase without using .islower()
output = ""
for char in user_input:     # Use for loop to check each char
    if "a" <= char <= "z":
        output = True
    else:
        output = False
print(output)