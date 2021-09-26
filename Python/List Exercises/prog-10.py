#List Manipulation Exercise 10 (Unique Elements From Multiple Lists)
#Write a function that accepts two input lists and returns a new list which contains only the unique elements from both lists.

def unique_elements_from_both_lists(list1,list2) :
       new_list=[]
       for elements in list1 :
              if elements not in new_list :
                     new_list.append(elements)
       for elements in list2 :
              if elements not in new_list :
                     new_list.append(elements)
       return new_list
