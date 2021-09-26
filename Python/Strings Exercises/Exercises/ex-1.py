#Strings Exercise 1 (Palindrome Test)
#Write a function that takes a string consisting of alphabetic characters as input argument and returns True if the string is a palindrome. A palindrome is a string which is the same backward or forward. Note that capitalization does not matter here i.e. a lower case character can be considered the same as an upper case character.

#Type 1
def palindrome_test(input_string) :
       reverse_string=""
       input_string_ignore_case=""
       for char in input_string :
              if (65<=ord(char)<=90) :
                     ascii_value=ord(char)+32
                     input_string_ignore_case+=chr(ascii_value)
              else :
                     input_string_ignore_case+=char
       for character in input_string_ignore_case :
              reverse_string=character+reverse_string
       if (input_string_ignore_case==reverse_string) :
              return True
       else :
              return False
              
#Type 2

def palindrome_test1(input_string) :
       if input_string.lower()== input_string[::-1].lower() :
              return True
       else :
              return False
