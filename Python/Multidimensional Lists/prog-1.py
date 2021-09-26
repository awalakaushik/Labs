#Multidimensional Lists Exercise 1 (Sum of a 2-D List)
#Write a function which accepts a 2D list of numbers and returns the sum of all the number in the list You can assume that the number of columns in each row is the same. (Do not use python's built-in sum() function).

def sum_of_num(numberlist):
    sum=0
    for list in numberlist:
        for num in list:
            sum+=num
    return sum