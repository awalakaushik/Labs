#Part 2: Find single insertion or deletion
#(1 point possible)
#Write a function named single_insert_or_delete that accepts two strings as input arguments and returns:

#0 if the two strings match exactly.
#1 if the first string can become the same as the second string by inserting or deleting a single character. Notice that inserting and deleting a character is not the same as replacing a character.
#2 otherwise
#Capital letters are considered the same as lower case letters. Here are some examples:
#First string	Second String	Function return
#Python	                         Java	2
#book	                         boot	2
#sin	                         sink	1 (Inserting a single character at the end)
#dog	                         Dog	0
#poke	                        spoke	1 (Inserting a single character at the start)
#poker	                        poke	1 (Deleting a single character from the end)
#programing	programming	1 (Inserting a single character)

def single_insert_or_delete(s1,s2):
       alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
       if s2.lower() == s1.lower():
              return 0
       elif s2.lower()!=s1.lower():
              for alphabet in alphabets:
                     if alphabet+s1.lower()==s2.lower() or s1.lower()+alphabet==s2.lower():
                            return 1
              for index in range(0,len(s1)):
                     if(s1[:index]+s1[index+1:]).lower()==s2.lower() :
                            return 1
                     for alphabet in alphabets:
                            if (s1[ : index]+alphabet+s1[index : ]).lower()==s2.lower():
                                   return 1
                            elif (s2[:index]+alphabet+s2[index:]).lower()==s1.lower():
                                   return 1
              return 2
#main program

print(single_insert_or_delete("Kaaushik","kaushik"))
print(single_insert_or_delete("sin","sink"))
print(single_insert_or_delete("dog","Dog"))
print(single_insert_or_delete("poke","spoke"))
print(single_insert_or_delete("poker","poke"))
print(single_insert_or_delete("programing","programming"))
print(single_insert_or_delete("Python","Java"))
print(single_insert_or_delete("book","boot"))
print(single_insert_or_delete("fan","fun"))

              
       
              
                            
                     
