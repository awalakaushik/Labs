#Strings Functions Exercise 1 (Leading White Space)
#Write a function that accepts an input string consisting of alphabetic characters and removes all the leading whitespace of the string and returns it without using .strip(). For example if:

#input_string = "    Hello  "
#then your function should return a string such as:
#output_string = "Hello  "

def remove_leading_whitespaces(string) :
       index_val=0
       for x in range(0,len(string)) :
              if string[x]!=" ":
                      index_val=x
                      break
       new_string=string[index_val::]
       return new_string
                      
                      
