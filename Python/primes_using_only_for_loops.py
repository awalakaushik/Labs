# A program to print all primes between 2 and 50 using only for loops

start_number=2
end_number=50
for number in range(start_number,end_number+1) :
       is_number_prime=True
       for divisor in range(2,number) :
              if number%divisor==0 :
                     is_number_prime=False
                     break
       if is_number_prime :
              print(number, " is a prime")
