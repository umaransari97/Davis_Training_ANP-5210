# Function to find the second largest score
def find_second_largest(numbers):
    # Removing duplicates first to ensure we get a different number than the max
    unique_numbers = list(set(numbers))
    # Sorting the list in ascending order
    unique_numbers.sort()
    # The second element from the end is the second largest
    return unique_numbers[-2]

# User input
nums = [int(x) for x in input("Enter numbers (spaces): ").split()]
# Displaying result
print(f"Output: {find_second_largest(nums)}")