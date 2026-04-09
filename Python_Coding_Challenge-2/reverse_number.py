def reverse_number(num):
    # Converting number to string
    num_str = str(num)
    # Reversing string by using slicing
    reversed_str = num_str[::-1]
    # Converting back to integer
    return int(reversed_str)


# Taking input from user
code = int(input("Enter a number: "))

# Calling function
reversed_code = reverse_number(code)

# Output
print(f"Output: {reversed_code}")
