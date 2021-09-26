#Write a function that takes a string consisting of alphabetic characters as input argument and returns the most common character. Ignore white spaces i.e. Do not count any white space as a character. Note that capitalization does not matter here i.e. that a lower case character is equal to a upper case character. In case of a tie between certain characters return the last character that has the most count

def most_common_character(input_string) :
       lower_case_string=input_string.lower().replace(" ","")
       print(lower_case_string)
       common_char=None
       max_count=0
       for char in lower_case_string:
              char_count=lower_case_string.count(char)
              if char_count>=max_count:
                     max_count=char_count
                     common_char=char
              return common_char
       
