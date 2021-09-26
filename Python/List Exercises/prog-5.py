#LIST MANIPULATION EXERCISE 5 (COUNTING AN ITEM IN A LIST)
#Write a function that accepts a list and a value of an element and returns the count of how many times that element appears in the list. The behaviour of this function should be exactly like the list.count() method. You may NOT use any built in list methods for this problem.

def element_count(list,value) :
       count=0
       for listelement in list :
              if value==listelement :
                     count+=1
       return count
