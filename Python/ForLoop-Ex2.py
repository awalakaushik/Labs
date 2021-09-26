#Using a for loop, write a program which asks the user to type an integer, n,
#and then prints the sum of all numbers from 1 to n(including both 1 and n).

user_response=input("Enter an integer: ")
number=int(user_response)
sum=0
for num in range(1, number + 1 ) :
       sum += num
print(sum)
