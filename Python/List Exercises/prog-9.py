#List Manipulation Exercise 9 (Unique Elements)
#Write a function that accepts an input list and returns a new list which contains only the unique elements(Elements should only appear one time in the list and the order of the elements must be preserved as the original list. ).

def retrieve_unique_elements(list1) :
       new_list=[]
       for element in list1 :
              if element not in new_list :
                     new_list.append(element)
       return new_list
