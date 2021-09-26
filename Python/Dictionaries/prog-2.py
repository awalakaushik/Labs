#Dictionary Exercise 2 (Sorted Values)
#Write a function that accepts a dictionary as input and returns a sorted list of all the values in the dictionary. Assume that the values of this dictionary are just integers.

def sortedvalues(dic):
    value_list=list(dic.values())
    value_list.sort()
    return value_list