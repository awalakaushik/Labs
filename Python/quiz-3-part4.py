#QUIZ 3, PART 4  (10 points possible)
#Write a function that accepts a list of integers as parameter. Your function should return the sum of all the odd numbers in the list. If there are no odd numbers in the list, your function should return 0 as the sum. 

#Remember that you are not asked to print anything. So, your function should just return the sum of all the odd numbers in the list. You do not need to call your function, it will automatically be called and tested for correctness with the test cases we provide. You only need to write one function and we will test your program with the first function that appears in your code. So, if you want to write more than one function to help you solve the problem, remember to embed the helper functions inside the first function.

def sum_of_odd(list_of_integers) :
       sum=0
       for x in list_of_integers :
              if (x%2)!=0 :
                     sum=sum+x
       return sum
       
