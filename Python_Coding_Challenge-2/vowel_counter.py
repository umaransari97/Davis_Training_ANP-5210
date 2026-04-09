def vowel_counter(str):
    count =0
    for x in str:
       if (str == "a" or str == "e" or str == "i" or str == "o" or str == "u"):
         count +=1
    return count;



#taking input form user, printing output and calling method to find total numbe rof vowels

print(f"Output: {vowel_counter(input("Enter a string:"))}")