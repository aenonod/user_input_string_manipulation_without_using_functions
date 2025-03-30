# Ask for user input with trailing whitespaces
user_input = input("Input your statement: ")

# Remove spaces without using .rstrip()
output = user_input
while output and output[-1] == " ":
    output = output[:-1]
print(output)