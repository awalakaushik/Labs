# A program to print all primes between 2 and 50 using while inside for loop

start_number=2
end_number=50
for number in range(start_number,end_number+1) :
       divisor=2
       is_number_prime=True
       while divisor<number :
              if number%divisor==0 :
                     is_number_prime=False
                     break
              divisor += 1
       if is_number_prime :
              print(number, " is a prime")
