#LIST METHODS EXERCISE 9 (LIST OF ODD NUMBERS)  
#Write a function that accepts two positive integers a and b and returns a list that contains all the odd numbers between a and b (including a and including b) in reverse order.

def reverse_odd_list(a,b) :
       rev_odd=[]
       for o in range(a,b+1) :
              if o%2 :
                     rev_odd.append(o)
       rev_odd.reverse()
       return rev_odd
