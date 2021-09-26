#Write a function that accepts a string of words separated by spaces consisting of alphabetic characters and returns a string such that each word in the input string is reversed while the order of the words in the input string is preserved. Capitalization does matter here. The length of the input string must be equal to the length of the output string i.e. there should be no trailing or leading spaces in your output string. For example if:

#input_string   = “this is a sample test”
#then the function should return a string such as:
#"siht si a elpmas tset"

def reverse_word_in_string(input_string):
       word_list=input_string.split()
       reverse_word=""
       reverse_string=""
       for word in word_list :
              for char in word :
                     reverse_word=char+reverse_word
              reverse_string+=reverse_word+" "
              reverse_word=""
       return reverse_string.rstrip()
