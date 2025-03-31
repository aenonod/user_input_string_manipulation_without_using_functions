# Ask for user input
user_input = input("Input text/number: ")

# Ask for a string to find
value = input("Input substring: ")

# Return the index without using .index()
position = 0
while True:
        position = user_input.find(value, position, len(user_input))

        if position == -1:
            print("Substring not found.")
            break
        output = print(f"Substring found at the index: {position}")
        break