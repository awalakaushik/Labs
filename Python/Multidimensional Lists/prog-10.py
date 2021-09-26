#Multidimensional Lists Exercise 10 (Sort Rows)
#Write a function that accepts a 2-dimensional list of integers, and sorts (descending order) all the elements inside each row and returns the sorted 2-dimensional list.

def sort_2d_desc(intlist):
    for row in intlist:
        row.sort(reverse=True)
    return intlist