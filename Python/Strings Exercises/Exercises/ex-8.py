#Write a function which accepts an input string and returns a string where every individual word in the input string is reversed and the case for every single character is reversed. The input string for this function would be a sentence (words separated by spaces) consisting of alphabetic characters. For example if:

#input_string = "Hello World"
#then the function should return a string such as:
#"DLROw OLLEh"

def reverse_string_and_case(input_string):
       reverse_case_string=""
       for char in input_string:
              if char.islower() :
                     reverse_case_string=char.upper()+reverse_case_string
              else:
                     reverse_case_string=char.lower()+reverse_case_string
       return reverse_case_string
              
       
