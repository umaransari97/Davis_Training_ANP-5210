# Declaring a list  for user input
sales = []

print("Enter sales for 7 days:")

for i in range(7):
    #taking user input
    amount = int(input(f"Day {i+1}: "))
    sales.append(amount)

# Calculating total weekly sales
total_sales = sum(sales)

# Output
print("Total Weekly Sales:", total_sales)