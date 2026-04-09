
def get_ticket_price(day):
    #Logic : Weekend usually cost more
    weekend =["Sunday", "Monday"]
    if day.capitalize() in weekend :
        return 200;
    else:
        return 150;

#input from user
day = input("Enter a day:")

#calling a method a prntng its output
print(f"Output: {get_ticket_price(day_input)}")