# method for vowel identifier
def vowel_identifier(char):
    if (char == "a" or char == "e" or char == "i" or char == "o" or char == "u"):
        return True
    else:
        return False

# Taking input from user
char = input("Enter a single character: ")

# checking whether a character is vowel or not
if (vowel_identifier(char)):
    print("Vowel")
else:
    print("Consonant")