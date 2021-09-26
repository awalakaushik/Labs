#Write a function that accepts a string and a character as input and returns the count of all the words in the string which start with the given character. Assume that capitalization does not matter here. You can assume that the input string is a sentence i.e. words are separated by spaces and consists of alphabetic characters.

def words_in_input_with_starting_char(input_string,character):
       word_count=0
       word_list=input_string.lower().split()
       for word in word_list :
              if (character==word[0]) :
                     word_count+=1
       return word_count
                     
