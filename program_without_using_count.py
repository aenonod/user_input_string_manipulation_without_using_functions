# Ask for user input
user_input = input("Input text/number: ")

# Ask for a string to count
word_to_count = input("Input text/number to count: ")

# Count the occurences of the specified string without using .count()
count = 0
position = 0
while True:
    position = user_input.find(word_to_count)
    
    if position == -1:
        break
    count += 1
    position += 1
print(count)