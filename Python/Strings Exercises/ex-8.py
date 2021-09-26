#Character Encoding Exercise 3 (Sum of Character Code Values)
#Write a function that accepts an alphabetic string and returns an integer which is the sum of all the UTF-8 codes of the character in that string. For example if the input string is "hello" then your function should return 532

def sumofstring(string) :
       sum=0
       for char in string :
              sum+=ord(char)
       return sum
