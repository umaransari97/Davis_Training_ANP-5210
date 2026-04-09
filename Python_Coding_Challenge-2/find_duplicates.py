# Function to find characters that appear more than once
def find_duplicates(text):
    # Characters store karne ke liye lists
    seen = []
    duplicates = []
    
    for char in text:
        # Agar character space nahi hai (spaces ko ignore karne ke liye)
        if char != " ":
            # Agar char pehle dekh chuke hain aur duplicates mein nahi dala hai
            if char in seen and char not in duplicates:
                duplicates.append(char)
            # Agar char naya hai toh 'seen' list mein dalo
            else:
                seen.append(char)
    
    # Duplicate characters ko space ke saath join karke return karna
    return " ".join(duplicates)

# User input
user_input = input("Enter a word: ")
# Result display karna
print(f"Output: {find_duplicates(user_input)}")