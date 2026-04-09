# Function to count total number of unique items
def count_unique_items(data_list):
    # A set only keeps unique values
    unique_set = set(data_list)
    # The length of the set is the count of unique elements
    return len(unique_set)

# User input
data = [int(x) for x in input("Enter numbers (spaces): ").split()]
# Displaying result
print(f"Output: {count_unique_items(data)}")