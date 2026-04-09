# Function to find the union of two sets
def find_union(set1, set2):
    # Union ka matlab hai saare unique elements dono sets se
    # '|' operator ya .union() method use kar sakte hain
    return set1 | set2

# User input for two sets
s1 = set(input("Enter first set elements (spaces): ").split())
s2 = set(input("Enter second set elements (spaces): ").split())

# Result display karna
print(f"Output: {find_union(s1, s2)}")