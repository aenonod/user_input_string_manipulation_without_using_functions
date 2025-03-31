# Ask for user input
user_input = input("Input text/number: ")

# Ask for a string to find
value = input("Input substring: ")

# Return the index without using .rindex()
position = len(user_input)
while True:
        position = user_input.find(value, 0, position)

        if position == -1:
            print("Substring not found.")
            break
        output = print(f"Substring found at the index: {position}")
        break