#Quiz 4, Part 2 (Count Consonants)
#(20 points possible)
#Write a function named count_consonants that receives a string as parameter and returns the total count of the consonants in the string. Consonants are all the characters in the english alphabet except for 'a', 'e', 'i', 'o', 'u'. If the same consonant repeats multiple times you should count all of them. Note that capitalization and punctuation does not matter here i.e. a lower case character should be considered the same as an upper case character.

def count_consonants(input_string) :
       count=0
       char_list=input_string.lower().split(" ")
       for char in char_list:
              for c in char :
                     if c not in ['a','e','i','o','u'] :
                            count+=1
       return count

#main program

print(count_consonants("Kaushik"))
