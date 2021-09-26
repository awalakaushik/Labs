# A program to print all primes between 2 and 50 using for inside while loop

start_number=2
end_number=50
number=start_number
while number<=end_number :
       is_number_prime=True
       for div in range(2,number) :
              if number%div == 0 :
                     is_number_prime=False
                     break
       if is_number_prime :
              print(number, " is a prime")
       number+=1
