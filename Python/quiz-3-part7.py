#Write a function that accepts two positive integers as function parameters and returns their least common multiple (LCM). The LCM of two integers a and b is the smallest (non zero) positive integer that is divisible by both a and b. For example, the LCM of 4 and 6 is 12, the LCM of 10 and 5 is 10. 

#Remember that you are not asked to print anything. So, your function should return the LCM and not print it. You do not need to call your function, it will automatically be called and tested for correctness with the test cases we provide. You only need to write one function and we will test your program with the first function that appears in your code. So, if you want to write more than one function to help you solve the problem, remember to embed the helper functions inside the first function.

def lcm_of_two_numbers(num1,num2) :
       n1=num1
       n2=num2
       #definition for finding the minimum of two numbers
       def least_of_the_two(num1,num2) :
              if (num1>num2) :
                     return num2 #returning num2 as the least num
              else :
                     return num1 #returning num1 as the least num
       least=least_of_the_two(n1,n2)
       while (True) :
              if ((least%num1==0) and (least%num2==0)) :
                     return least
              else :
                     least+=1
              
