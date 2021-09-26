#Multidimensional Lists Exercise 3 (Maximum Even Value of a 2-D List)
#Write a function that accepts a 2D list of integers and returns the maximum EVEN value for the entire list. You can assume that the number of columns in each row is the same. Your function should return None if the list is empty or all the numbers in the 2D list are odd. Do NOT use python's built in max() function.

def max_even(intlist) :
    even_list=[]
    if not intlist:
        return
    if len(intlist)>0:
        for list in intlist:
            for num in list:
                if (num%2==0):
                    even_list.append(num)
        if not even_list:
            return        
        even_max=even_list[0]
        for even in even_list:
            if even>even_max:
                even_max=even
        return even_max
    return
                     