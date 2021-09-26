#Midterm Exam, Part 10 (Numbers To Words)
#(10 points possible)
#Write a program that asks the user to enter an integer between 1 and 9999 (both inclusive) and then prints the input integer using words. For example if the user enters:

#3421
#Then your program should print
#three thousand four hundred twenty one
#more examples:
#Input	Printed Output
#15	fifteen
#7000	seven thousand
#501	five hundred one
#1008	one thousand eight
#7	seven
#Notes:
#the words in the printed output should all be lower cased and separated by only one space
#There is no "and" between the printed words.
#Notice that when you use a print() statement, Python by default adds a new line after each printed output. If you do not want each new print statment to be printed in a new line then you should add end="" at the end of your print arguments as shown below:
#print("seven ", end = "")
#print("thousand")
#This will print
#seven thousand
#Also when you use two arguments in a print statement, Python adds a space between them by default. For example:
#print("x",5)
#will print
#x 5
#If you do not want a space to be inserted between your arguments then you should add sep="" at the end of your print arguments as shown below:
#print("x",5,sep="")
#will print
#x5
#Make sure your words match the following spellings:
#one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen,
#sixteen, seventeen, eighteen, nineteen, twenty, thirty, forty, fifty, sixty, seventy, eighty,
#ninety, hundred, thousand

#reading the number from the user
n=int(input("Enter a number between 1 and 9999: "))
#function to convert a number that is greater than 1000
def convert(number) :
       prefix=""
       current=""
       group1=["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
       group2=["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
       group3=["","thousand"]
       #function to convert a number that is less than 1000
       def convert_less_than_thousand(number) :
              if number%100 < 20 :
                     current=group1[number%100]
                     number//=100
              else:
                     current=group1[number%10]
                     number//=10
                     current=group2[number%10]+' '+current
                     number//=10
              if number==0 :
                     return current
              return group1[number]+" hundred "+current
       #back to convert function!
       n=number%1000
       if n!=0 :
              s=convert_less_than_thousand(n)
              current=s+' '+group3[0]+' '+current
       number//=1000
       while number>0 :
              n=number%1000
              if n!=0 :
                     s=convert_less_than_thousand(n)
                     current=s+' '+group3[1]+' '+current
              number//=1000
       return (prefix+current).rstrip()
#main function to convert the entered number into equi word format
word=convert(n)
print(word)
