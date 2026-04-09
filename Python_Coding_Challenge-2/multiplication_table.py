def print_table(n):
    # Loop runs from 1 to 10
    for i in range(1, 11):
        # Multiplying the number by loop index (1 to 10)
        # end=" " delimiter is used to print results in a single row
        print(n * i, end=" ")
    # New line after the table is complete
    print()

# Taking number as input from the user
table_num = int(input("Enter number for table: "))

# Calling the function to display the table
print_table(table_num)