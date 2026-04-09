def is_palindrome(text):
    reversed_text = text[::-1] # String ko reverse karne ka shortcut
    if text.lower() == reversed_text.lower():
        return "Yes"
    else:
        return "No"

#taking input form user, printing output and calling method
print(f"Output: {is_palindrome(input("Enter a string:"))}")