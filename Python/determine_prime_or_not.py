# A program to determine whether a number is prime or not

current_number=23
current_divisor=2
is_current_number_prime=True
while(current_divisor<current_number) :
       if current_number%current_divisor == 0 :
              is_current_number_prime=False
              break
       current_divisor=current_divisor + 1
if is_current_number_prime :
       print(current_number, " is prime")
else :
       print(current_number, " is not prime")
