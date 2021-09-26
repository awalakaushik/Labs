#Multidimensional Lists Exercise 4 (List of Sum of Rows of a 2-D List)
#Write a function that takes a two-dimensional list (list of lists) of numbers as argument and returns a list which includes the sum of each row. You can assume that the number of columns in each row is the same.

def row_sum(intlist):
    row_sum_list=[]
    for list in intlist:
        sum=0
        for num in list:
            sum+=num
        row_sum_list.append(sum)
    return row_sum_list