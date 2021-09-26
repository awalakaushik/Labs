#Write a function which accepts an input string and returns a string where the case of the characters are changed, i.e. all the uppercase characters are changed to lower case and all the lower case characters are changed to upper case. The non-alphabetic characters should not be changed. Do NOT use the string methods upper(), lower(), or swap().

def change_cases(input_string):
       new_list=[]
       for i in input_string:
              if (65<=ord(i)<=90):
                     ascii_value=ord(i)+32
                     new_list.append(chr(ascii_value))
              elif (97<=ord(i)<=122):
                     ascii_value=ord(i)-32
                     new_list.append(chr(ascii_value))
              else :
                     new_list.append(i)
       return "".join(new_list)
