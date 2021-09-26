#Write a function named multiplication_table that receives a positive integer 'n' as parameter and returns a n by n multiplication table as a two-dimensional list. 

#For example if the integer received by the function 'n' is:

#4
#then your program should return a two_dimensional list with 4 rows and 4 columns such as:
#[[1, 2, 3, 4],
 #[2, 4, 6, 8],
 #[3, 6, 9, 12],
 #[4, 8, 12, 16]]
 
def multiplication_table(n):
    outputlist=[[] for i in range(n)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            outputlist[i-1].append(i*j)
    return outputlist

#main
print(multiplication_table(4))