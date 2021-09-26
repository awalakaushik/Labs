#LIST METHODS EXERCISE 8 (LIST OF EVEN NUMBERS)  
#Write a function that accepts two positive integers a and b and returns a list of all the even numbers between a and b (including a and not including b).

def list_even_numbers(a,b) :
       even_numbers=[]
       for e in range(a,b) :
              if not e%2 :
                     even_numbers.append(e)
       return even_numbers
