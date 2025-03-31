# Ask for user input
user_input = input("Input your statement: ")

# Check is user input is uppercase without using .isupper()
output = True
for char in user_input:     # Use for loop to check each char
    if not "A" <= char <= "Z":
        output = False
        break
print(output)