#Multidimensional Lists Exercise 5 (List of Sum of Columns of a 2-D List)
#Write a function that takes a two-dimensional list (list of lists) of numbers as argument and returns a list which includes the sum of each column. Assume that the number of columns in each row is the same.

def col_sum(intlist):
    cols = len(intlist[0])
    mylist = []
    for c in range(cols):
        column_sum = 0
        for row in intlist:
            column_sum += row[c]
        mylist.append(column_sum)
    return mylist