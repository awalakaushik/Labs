#List Manipulation Exercise 8 (Adding Odds from 2 Lists)
#Write a function that accepts two lists both of which consists of integers and returns the total sum of all the odd integers from both lists.

def sum_of_odd_of_two_lists(list1,list2) :
       list1.extend(list2)
       sum=0
       for integer in list1 :
              if integer%2!=0 :
                     sum+=integer
       return sum
