#LIST METHODS EXERCISE 11 (LIST OF DIVISORS)  
#Write a function that accepts a positive integer k and returns the list of all the divisors of k. Your list should include both 1 and k.

def divisors_list(k) :
       list_div=[]
       for div in range(1,k+1) :
              if k%div == 0 :
                     list_div.append(div)
       return list_div
