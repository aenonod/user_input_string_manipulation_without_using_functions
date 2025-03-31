# Ask for user input
user_input = input("Input your statement: ")

# Check if user input is lowercase without using .islower()
output = True
for char in user_input:     # Use for loop to check each char
    if not "a" <= char <= "z":
        output = False
        break
print(output)