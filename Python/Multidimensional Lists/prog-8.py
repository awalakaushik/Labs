#Multidimensional Lists Exercise 8 (List of Column Maximums)
#Write a function that takes a two-dimensional list (list of lists) of numbers as argument and returns a list which includes the maximum value of each column. Assume that the length of columns is consistent in each row.

def col_max(intlist):
    cols = len(intlist[0])
    col_max_list = []
    for c in range(cols):
        column_max = 0
        for row in intlist:
            if column_max < row[c]:
                column_max=row[c]
        col_max_list.append(column_max)
    return col_max_list