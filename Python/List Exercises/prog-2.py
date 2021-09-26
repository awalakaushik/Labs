#LIST MANIPULATION EXERCISE 2 (EXTENDING A LIST WITHOUT LIST FUNCTIONS)
#Write a function that accepts two lists A and B and returns a new list which contains all the elements of list A followed by elements of list B. Notice that the behaviour of this function is different from list.extend() method because the list.extend() method extends the list in place, but here you are asked to create a new list and return it. Your function should not return the original lists. For example if the input lists are:

#A = ['p', 'q', 6, 'k']
#B = [8, 10]
#Then your function should return a list such as:
#['p', 'q', 6, 'k', 8, 10]

def append_two_lists(list1,list2) :
       newlist=[]
       for item in list1 :
              newlist.append(item)
       for item in list2 :
              newlist.append(item)
       return newlist
