#Write a function which returns the number of words in the input string which have more than 4 characters. Assume that the input string consists of alphabetic characters separated by spaces and capitalization does not matter i.e. an upper case character should be treated the same as a lower case character.

def num_of_words_of_specific_length(input_string):
       word_list=input_string.lower().split()
       print(word_list)
       word_count=0
       for word in word_list:
              if len(word)>4 :
                     word_count+=1
       return word_count
