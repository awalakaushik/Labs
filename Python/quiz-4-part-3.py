#Quiz 4, Part 3 (Longest Word)
#(20 points possible)
#Write a function named find_longest_word that receives a string as parameter and returns the longest word in the string. Assume that the input to this function is a string of words consisting of alphabetic characters that are separated by space(s). In case of a tie between some words return the last one that occurs.

def find_longest_word(input_string) :
       word_list=input_string.split(" ")
       longest_word=' '
       for word in word_list:
              if len(word)>len(longest_word) :
                     longest_word=word
              if len(word)==len(longest_word) :
                     longest_word=word
       return longest_word

#main program
print(find_longest_word("why is this quiz so easy"))
