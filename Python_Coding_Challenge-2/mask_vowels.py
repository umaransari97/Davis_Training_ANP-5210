# Function to replace vowels with *
def mask_vowels(text):
    # Saare vowels ki string (small aur capital dono)
    vowels = "aeiouAEIOU"
    # Result store karne ke liye khali string
    result = ""
    
    # String ke har character ko check karne ke liye loop
    for char in text:
        # Agar character vowel list mein hai
        if char in vowels:
            # Toh '*' add karo
            result += "*"
        else:
            # Warna wahi character rehne do
            result += char
    return result

# User input lena
user_text = input("Enter a word: ")
# Result dikhana
print(f"Output: {mask_vowels(user_text)}")