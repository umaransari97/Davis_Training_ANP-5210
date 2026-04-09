# Function to find a missing number in a sequence
def find_missing_number(num_list):
    # Sequence ki range start se end tak honi chahiye
    n = len(num_list) + 1 # Total elements hone chahiye n
    # Expected sum using mathematical formula: n*(n+1)/2
    # Par hum range use karenge sequence ke liye
    full_range_sum = sum(range(min(num_list), max(num_list) + 1))
    actual_sum = sum(num_list)
    
    # Difference hi missing number hai
    return full_range_sum - actual_sum

# User input
nums = [int(x) for x in input("Enter sequence with one missing number (e.g., 1 2 4 5): ").split()]
print(f"Output: {find_missing_number(nums)}")