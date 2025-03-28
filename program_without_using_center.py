# Ask for user input
user_input = input("Input your statement: ")

# Ask for width of string
width = int(input("Input width where the string is centered: "))

# Centered the string without using .center()
# Calculate how much padding is needed
padding_needed = width - len(user_input)

if padding_needed <= 0:
    print(user_input)
else:     # Split the padding
    left_padding = padding_needed // 2
    right_padding = padding_needed - left_padding

    centered_str = " " * left_padding + user_input + " " * right_padding
    print(centered_str)