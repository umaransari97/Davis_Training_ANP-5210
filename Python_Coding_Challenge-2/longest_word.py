# Function to find the longest word in a sentence
def find_longest_word(sentence):
    # sentence.split() sentence ko words ki list mein tod deta hai
    words = sentence.split()
    # Initializing longest word as an empty string
    longest = ""
    
    # Har word ko check karne ke liye loop
    for word in words:
        # Agar current word ki length 'longest' se zyada hai
        if len(word) > len(longest):
            # Toh usse naya longest word maan lo
            longest = word
    # Final result return karo
    return longest

# User se sentence input lena
user_input = input("Enter a sentence: ")
# Function call aur output print karna
print(f"Output: {find_longest_word(user_input)}")