def is_palindrome(num):
    # A palindrome reads the same forward and backward
    # First, convert number to string
    original = str(num)
    # Reverse the string using slicing
    reversed_ver = original[::-1]
    
    # Compare the original string with the reversed string
    if original == reversed_ver:
        # If they match, it is a palindrome
        return "Palindrome"
    else:
        # If they don't match, it is not
        return "Not a Palindrome"

# Testing with the example input
test_num = 121
# Calling the function and printing result
print(f"Output: {is_palindrome(test_num)}")