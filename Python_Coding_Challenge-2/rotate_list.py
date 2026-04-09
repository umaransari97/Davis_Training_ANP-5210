# Function to rotate list by one position to the right
def rotate_list(my_list):
    if not my_list:
        return my_list
    # Last element ko pehle lana aur baaki elements ko piche shift karna
    # Slicing: [last_item] + [all_except_last]
    rotated = [my_list[-1]] + my_list[:-1]
    return rotated

# User input
data = [int(x) for x in input("Enter list elements (spaces): ").split()]
print(f"Output: {rotate_list(data)}")