#LIST METHODS EXERCISE 7 (LIST OF MULTIPLES)  
#Write a function that accepts a positive integer k and returns a list that contains the first five multiples of k. The multiples should be calculated starting from 1 to 5 (including both 1 and 5). For example the first five multiples of 3 are 3, 6, 9, 12, and 15

def multiples_of_num(k) :
       list_multiples=[]
       for m in range(1,6) :
              list_multiples.append(k*m)
       return list_multiples
