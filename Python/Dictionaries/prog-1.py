#Dictionary Exercise 1 (Sorted Keys)
#Write a function that accepts a dictionary as input and returns a sorted list of all the keys in the dictionary.

def sortedlist(dic):
    key_list=list(dic.keys())
    key_list.sort()
    return key_list