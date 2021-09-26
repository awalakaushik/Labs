#Midterm Exam, Part 4 (List of Primes)
#(10 points possible)
#Write a function named list_of_primes that accepts a positive integer n and returns a sorted list (ascending order) of all the prime numbers between 2 and n (including 2 but not including n)

def list_of_primes(n) :
       new_list=[]
       for i in range(2,n) :
              count=0
              for j in range(1,i+1):
                     if i%j == 0 :
                            count+=1
              if count==2 :
                     new_list.append(i)
       return new_list
