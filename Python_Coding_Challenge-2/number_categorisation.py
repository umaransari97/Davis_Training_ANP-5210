#Number Categorisation 
#method for categorisation of number
def categorize_number (n):
    if n <0:
        return "Positive"
    elif(n<0):
        return "Negative"
    else:
        return "Zero"
    
#Takng input from user    
num = int(input("Enter a number: "))

#printing output after categorisation by using f string
print(f"{num} is {categorize_number(num)}")