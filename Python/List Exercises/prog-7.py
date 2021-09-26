#List Manipulation Exercise 7 (Modifying a List)
#Write a function that accepts a list that contains positive integers and returns a new list which contains all the elements from original list but adds 1 to those elements which are odd. For example if :

#input_list = [12, 3, 4, 5, 6]
#Then your function should return a list such as:
#[12, 4, 4, 6, 6]

def add_one_to_odd(list_of_integers) :
       new_list=[]
       for integer in list_of_integers :
              if integer%2 != 0 :
                     integer=integer+1
                     new_list.append(integer)
              else :
                     new_list.append(integer)
       return new_list
