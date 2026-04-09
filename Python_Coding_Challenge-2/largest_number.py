def find_largest(a, b, c):
    # Returns the maximum value among three numbers
    return max(a, b, c)

# Input and Function Call
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))

print(f"Largest: {find_largest(n1, n2, n3)}")