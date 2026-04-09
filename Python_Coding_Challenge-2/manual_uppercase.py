# Function to convert lowercase to uppercase without .upper() method
def to_uppercase(text):
    # Empty string to build the uppercase result
    final_string = ""
    # Loop through each character in input
    for char in text:
        # Check if character is a lowercase letter (ASCII 97-122)
        if 'a' <= char <= 'z':
            # Convert to uppercase by subtracting 32 from its ASCII value
            # ord() gets ASCII number, chr() converts number back to letter
            final_string += chr(ord(char) - 32)
        else:
            # If it's already upper or a symbol, keep it as it is
            final_string += char
    # Return the converted string
    return final_string

# Take lowercase input from user
user_input = input("Enter a lowercase string: ")
# Call function and display uppercase result
print(f"Output: {to_uppercase(user_input)}")