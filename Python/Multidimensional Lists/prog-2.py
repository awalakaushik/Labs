#Multidimensional Lists Exercise 2 (Average of a 2-D List)
#Write a function that accepts a 2 Dimensional list of integers and returns the average. Remember that average = (sum_of_all_items) / (total_number_of_items). sum_of_all_items in this case would be the sum of all individual integers from all the rows. To calculate the average for this problem, use the number of rows as the total_number_of_items. Assume that the number of columns in each row is the same.

def avg(integerlist):
    sum=0
    length=len(integerlist)
    for list in integerlist:
        for num in list:
            sum+=num
    return (sum/length)