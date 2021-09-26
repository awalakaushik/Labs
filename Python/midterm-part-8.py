#Midterm Exam, Part 8 (Unique Common Elements)
#(10 points possible)
#Write a function named unique_common that accepts two lists both of which contain integers as parameters and returns a sorted list (ascending order) which contains unique common elements from both the lists. If there are no common elements between the two lists, then your function should return the keyword None 

#For example, if two of the lists received by the function are:

#([5, 6, -7, 8, 8, 9, 9, 10], [2, 4, 8, 8, 5, -7])
#You can see that elements 5, -7, and 8 are common in both the first list and the second list and that the element 8 occurs twice in both lists. Now you should return a sorted list (ascending order) of unique common elements like this:
#[-7, 5, 8]
#if the two lists received by the function are:
#([5, 6, 7, 0], [3, 2, 3, 2])
#Since, there are no common elements between the two lists, your function should return the keyword
#None

def unique_common(a,b) :
       unique_list=[]
       for a_el in a : #el stands for element
              for b_el in b:
                     if (a_el == b_el) and (a_el not in unique_list) :
                            unique_list.append(a_el)
       if not unique_list :
               return
       else :
              unique_list.sort()
              return unique_list
       
