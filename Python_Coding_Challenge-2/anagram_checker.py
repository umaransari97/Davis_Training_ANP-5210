# Function to check if two strings are anagrams
def check_anagram(str1, str2):
    # Anagrams wo hote hain jinme same characters ho (jaise listen aur silent)
    # Dono strings ko sort karke compare karna sabse asan hai
    # sorted() function characters ko alphabet wise arrange kar deta hai
    return sorted(str1.lower()) == sorted(str2.lower())

# Do strings input lena
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

# Result check karna
if check_anagram(word1, word2):
    print("Output: True")
else:
    print("Output: False")
    