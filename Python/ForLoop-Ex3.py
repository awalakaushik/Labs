#Using a for loop, write a program which asks the user to type an integer, n, and then prints the sum of the square of all numbers form 1 to n (including both 1 and n).

#For example if the user type 3, the answer should be ((3**2) + (2**2) + (1**2)) = 14

number = int( input("Enter a number: ") )
sum = 0
for num in range(1,number+1) :
       sum += num**2
print(sum)
