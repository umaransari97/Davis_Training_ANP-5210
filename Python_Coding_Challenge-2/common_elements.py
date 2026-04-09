# Function to find common elements between two lists
def find_common(list1, list2):
    # Using list comprehension to find elements that are in both lists
    common = [item for item in list1 if item in list2]
    # Removing duplicates from common list if any
    return list(set(common))

# Taking two lists as input
list_a = [int(x) for x in input("Enter first list (spaces): ").split()]
list_b = [int(x) for x in input("Enter second list (spaces): ").split()]

# Printing the common values
print(f"Output: {find_common(list_a, list_b)}")