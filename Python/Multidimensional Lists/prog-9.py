#Multidimensional Lists Exercise 9 (2D To 1D)
#Write a function that accepts a 2-dimensional list of integers, and returns a sorted (ascending order) 1-Dimensional list containing all the integers from the original 2-dimensional list.

def sort_2d_to_1d(intlist):
    list_1d=[]
    for sublist in intlist:
        for num in sublist:
            list_1d.append(num)
    list_1d.sort()    
    return list_1d