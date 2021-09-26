#Quiz 4, Part 4 (Anagrams Test)
#(20 points possible)
#Write a function named test_for_anagrams that receives two strings as parameters, both of which consist of alphabetic characters and returns True if the two strings are anagrams, False otherwise. Two strings are anagrams if one string can be constructed by rearranging the characters in the other string using all the characters in the original string exactly once. For example, the strings "Orchestra" and "Carthorse" are anagrams because each one can be constructed by rearranging the characters in the other one using all the characters in one of them exactly once. Note that capitalization does not matter here i.e. a lower case character can be considered the same as an upper case character

def test_for_anagrams(my_string1, my_string2):
       my_string1=my_string1.lower()
       my_string2=my_string2.lower()
       string1_chars=[]
       string2_chars=[]
       for char in my_string1:
              string1_chars.append(char)
       for char in my_string2:
              string2_chars.append(char)
       for char in string1_chars and string2_chars :
              if char in string1_chars and char in string2_chars :
                     anagram=True
              else:
                     anagram=False
                     break
       return anagram
#main program
print(test_for_anagrams("karthiK","KarthiK"))
              
