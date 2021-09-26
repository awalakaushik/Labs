#Write a program that asks the user for an input 'n' (assume that the user enters a positive integer) and prints only the boundaries of the triangle using asterisks "*" of height 'n'. For example if the user enters 6 then the height of the triangle should be 6 as shown below and there should be no spaces between the asterisks on the top line:

#******
#*   *
#*  *
#* *
#**
#*

n = int(input("Please enter a positive integer: "))
if n > 1:
    print (n*"*") # Print the top line
    for x in range(n-1, 1, -1):
        print("*"+ (x-2)*" "+"*") # Print the middle lines
    print("*") #print the bottom line
elif n == 1:
    print("*")
