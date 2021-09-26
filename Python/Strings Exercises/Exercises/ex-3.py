#Write a function which returns the total number of vowels in an input string which consists of alphabetic characters. Note that capitalization does not matter here i.e. a lower case character should be considered the same as an upper case character.

def number_of_vowels(input_string):
       vowel_count=0
       for character in input_string:
              if(character=="A" or character=="a"or character=="E" or character=="e" or character=="I" or character=="i" or character=="O" or character=="o" or character=="U" or character=="u") :
                     vowel_count+=1
       return vowel_count
