#Write a function that accepts a string and a character as input and returns the number of times the character is repeated in the string. Note that capitalization does not matter here i.e. a lower case character should be treated the same as an upper case character.

def character_no_in_input_str(input_string,character) :
       char_count=0
       for char in input_string :
              if(char==character.lower()) :
                     char_count+=1
       return char_count
