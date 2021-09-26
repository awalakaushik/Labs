#Write a program using while loop, which asks the user to type a positive integer, n, and then prints the factorial of n.
#A factorial is defined as the product of all the numbers from 1 to n (1 and n inclusive)

user_response = input("Enter a positive integer: ")
number = int(user_response)
factorial = 1
while number >= 1 :
       factorial *= number
       number -= 1
print(factorial)
