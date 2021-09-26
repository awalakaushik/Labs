#Multidimensional Lists Exercise 7 (List of Row Maximums)
#Write a function that takes a two-dimensional list (list of lists) of numbers as argument and returns a list which includes the maximum value of each row.

def row_max(intlist):
    row_max_list=[]
    for sublist in intlist:
        maxval=0
        for num in sublist:
            if maxval<num:
                maxval=num
        row_max_list.append(maxval)
    return row_max_list