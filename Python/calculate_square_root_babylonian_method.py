#This program finds the square root of a number using a babylonian method or algorithm

user_response=input("Enter a number: ")
number=float(user_response)
accuracy=0.0001
iteration=0
guess=number/2
while abs(number-(guess**2))>accuracy :
       print("Iteration: ",iteration+1)
       guess=(guess+(number/guess))/2
       print("Guessed square root is : ",guess)
       iteration+=1
print(" ")
print("Original number is : ",number)
print("Square root of ",number," is : ",guess)
