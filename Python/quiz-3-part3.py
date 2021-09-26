#QUIZ 3, PART 3  (10 points possible)
#Write a program that asks the user for a positive number 'n' as input.
#Assume that the user enters a number greater than or equal to 3 and print a triangle as described below. F
#or example if the user enters 6 then the output should be:
#*
#**
#***
#****
#*****
#******
#*****
#****
#***
#**
#*
#Note that, there should be no spaces between the asterisks (*))

n=int(input("Enter a number: "))
#for i in range(1,n+1) :
  #     for j in range(1,i+1) :
    #          print ("*",end="")
      # print("")
#for i in range(n-1,0,-1) :
  #     for j in range (1,i+1) :
    #          print("*",end="")
      # print("")
for i in range(1,n+1) :
       print("*" * i)
for j in range(n-1,0,-1) :
       print("*" * j)
