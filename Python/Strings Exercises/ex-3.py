#Strings, Exercise 3
#Write a program using while loops that asks the user for a positive integer 'n' and prints a triangle using numbers from 1 to 'n'. For example if the user enters 6 then the output should be like this :

#(There should be no spaces between the numbers)

#1
#22
#333
#4444
#55555
#666666

n=int(input("Enter an integer n: "))
i=1
while i<=n :
       print(str(i)*i)
       i+=1
