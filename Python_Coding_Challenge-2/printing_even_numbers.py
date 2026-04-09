def print_even_numbers(n):
    # Using a for loop to iterate from 1 up to n.
    for i in range(1, n + 1):
        # Checking if the number is divisible by 2 with 0 remainder
        if i % 2 == 0:
            # Printing the number; 'end=" "' keeps the output on the same line
            print(i, end=" ")
    # Printing an empty line at the end for clean formatting
    print()

# Calling the function to display even numbers
print_even_numbers(int(input("Enter limit for calculating even numbers:")))