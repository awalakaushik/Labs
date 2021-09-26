#Using a for loop, write a program which prints the sum of all the even numbers from 1 to 101.
sum=0
for number in range(1,101) :
       if number % 2 == 0 :
              sum += number
print(sum)
