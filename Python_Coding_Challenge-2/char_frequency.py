# Function to count how many times a character appears in a string
def count_character(text, target):
    # Use built-in count() method for the specific character
    count = text.count(target)
    # Return the frequency count
    return count

# Input for the full string
user_string = input("Enter the word (e.g., banana): ")
# Input for the character to count
user_char = input("Enter the character to count (e.g., a): ")

# Execute function and show result
print(f"Output: {count_character(user_string, user_char)}")