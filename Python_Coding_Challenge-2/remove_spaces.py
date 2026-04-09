# Function to remove all white spaces from a string
def remove_spaces(text):
    # Use replace() method to find spaces and replace them with empty string
    clean_text = text.replace(" ", "")
    # Return the string without spaces
    return clean_text

# Get input from user (e.g., "hello world")
user_input = input("Enter a string with spaces: ")
# Print the result inside quotes to see the change clearly
print(f"Output: '{remove_spaces(user_input)}'")