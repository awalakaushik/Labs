#Part 1: Find mismatch
#(1 point possible)
#Write a function named find_mismatch that accepts two strings as input arguments and returns:

#0 if the two strings match exactly.
#1 if the two strings have the same length and mismatch in only one character.
#2 if the two strings do not have the same length or mismatch in two or more characters.
#Capital letters are considered the same as lower case letters. Here are some examples:
#First string	Second String	Function return
#Python	                          Java	2
#Hello There	          helloothere	1
#sin	                          sink	2 (note not the same length)
#dog	                          Dog	0

def find_mismatch(s1,s2):
       if(len(s1)!=len(s2)):
              return 2
       if(len(s1)==len(s2)):
              mismatch=0
              for i in range(0,max(len(s1),len(s2))):
                     if(s1[i].lower()!=s2[i].lower()):
                            mismatch+=1
              if mismatch==1:
                     return 1
              elif mismatch>=2:
                     return 2
              else:
                     return 0
# main program
print(find_mismatch("Python","Java"))
print(find_mismatch("Hello There","helloothere"))
print(find_mismatch("sin","sink"))
print(find_mismatch("dog","Dog"))
