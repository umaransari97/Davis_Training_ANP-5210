# Function to sort a list using Bubble Sort (No .sort() used)
def bubble_sort_manual(my_list):
    n = len(my_list)
    # Outer loop to traverse through all elements
    for i in range(n):
        # Inner loop for comparisons
        for j in range(0, n - i - 1):
            # If current element is greater than the next, swap them
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list

# User input
unordered_list = [int(x) for x in input("Enter numbers to sort (spaces): ").split()]
# Sorting and printing
print(f"Output: {bubble_sort_manual(unordered_list)}")