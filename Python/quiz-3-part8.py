#QUIZ 3, PART 8  (10 points possible)
#Write a function that accepts two positive integers as parameters. The first integer is the number of heads and the second integer is the number of legs of all the creatures in a farm which consists of chickens and dogs. Your function should calculate and return the number of chickens and number of dogs in the farm in a list as specified below. If it is impossible to determine the correct number of chickens and dogs with the given information then your function should return None. Example 1, if your function received the following numbers:

#5, 12 
#This means that someone has counted a total of 5 heads and total of 12 legs in the farm. Now, your function should calculate how many chickens and how many dogs are in the farm and return that information in a list exactly as shown below.
#[4, 1] 
#this means that there were 4 chickens and 1 dog in the farm. 

#Example 2, if your function received the following numbers:
#7, 12 
#Then it should return:
#None 


#Remember that you are not asked to print anything. So, your function should return a list that contains two numbers exactly in this order [number_of_chickens, number_of_dogs] not print it. You do not need to call your function, it will automatically be called and tested for correctness with the test cases we provide. You only need to write one function and we will test your program with the first function that appears in your code. So, if you want to write more than one function to help you solve the problem remember to embed the helper functions inside the first function.

def num_of_chicks_and_dogs(heads,legs) :
       if ((legs>=heads*2) and (legs<=heads*4)) :
              if (legs%2) == 0 :
                     dogs=(legs/2)-heads
                     chickens=heads-dogs
                     return [chickens,dogs]
       else :
              return
       
