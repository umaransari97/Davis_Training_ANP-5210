# Function to count total words in a sentence
def count_words(sentence):
    # .split() extra spaces ko ignore karke words ki list banata hai
    words_list = sentence.split()
    # List ki length hi words ka total count hai
    return len(words_list)

# User input
user_sentence = input("Enter a sentence: ")
# Count print karna
print(f"Output: {count_words(user_sentence)}")