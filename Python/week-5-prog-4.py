#LIST METHODS EXERCISE 10 (LIST OF CUBE ROOTS))  
#Write a function that accepts a positive integer k and returns the list of cube root values of all the numbers from 1 to k (including 1 and not including k). [if k is 1, your program should return an empty list]

def cube_root_list(k) :
       cube_list=[]
       if k==1 :
              return cube_list
       else :
              for num in range(1,k) :
                     cube_list.append(num**(1/3))
              return cube_list
