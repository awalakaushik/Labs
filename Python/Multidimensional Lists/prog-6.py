#Multidimensional Lists Exercise 6 (Count Rows with Even and Odd Sums)
#Write a function that will receive a 2D list of integers. The function should return the count of how many rows of the list have even sums and the count of how many rows have odd sums. For example if the even count was 2, and odd count was 4 your function should return them in a list like this: [2, 4].

def even_odd_row_count(intlist):
    evencount=0
    oddcount=0
    resultlist=[]
    for sublist in intlist:
        sum=0
        for num in sublist:
            sum+=num
        if sum%2==0:
            evencount+=1
        else: 
            oddcount+=1
    resultlist.append(evencount)
    resultlist.append(oddcount)
    return resultlist