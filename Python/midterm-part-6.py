#Midterm Exam, Part 6 (ListsiL)
#(10 points possible)
#Write a function named crazy_list that accepts a list as parameter and returns a boolean (either True or False) based on whether or not the list is the same forward and backwards. You may NOT use list.reverse() method. 

#For example, if the list received by the function is:

#[5, 6, 8, 9, 'PYTHON', 9, 8, 6, 5] 
#(Notice how the list is exactly the same whethere you read it from left to right, or from right to left) Then your function should return the Boolean
#True 
#however, if the list recieved by the function is something like this:
#[4, 5, 6, 7, 8, 4, 5, 2] 
#(Notice how the list is NOT the same when reading from left to right vs right to left) In this case, your function should return the Boolean
#False 

def crazy_list(some_list) :
       rev_list=some_list[-1::-1]
       i=0
       for x in some_list :
              if some_list[i]!=rev_list[i] :
                     return False
              i+=1
       return True
