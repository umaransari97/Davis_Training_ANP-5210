# Function to find common elements (intersection)
def find_intersection(set1, set2):
    # Intersection ka matlab hai wo elements jo dono sets mein common hon
    # '&' operator intersection nikalta hai
    return set1 & set2

# User input
s1 = set(input("Enter first set elements (spaces): ").split())
s2 = set(input("Enter second set elements (spaces): ").split())

print(f"Output: {find_intersection(s1, s2)}")