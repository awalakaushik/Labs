# A program to print all the prime numbers
# between 2 and 50

start_number=2
end_number=50
number=start_number
while number < end_number :
       divisor=2
       is_number_prime=True
       while divisor < number :
              if number%divisor==0 :
                     is_number_prime=False
                     break
              divisor += 1
       if is_number_prime :
              print(number, " is a prime")
       number += 1
print("Finished finding the primes between ", start_number, " and ", end_number)
