#method for checking leap year
def check_leap_year(year):
    # A year is a leap year if divisible by 4
    # But centuries (like 1900) must be divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap Year"
    else:
        return "Not a Leap Year"

# Input and Function Call
year = int(input("Enter year: "))
print(check_leap_year(year))