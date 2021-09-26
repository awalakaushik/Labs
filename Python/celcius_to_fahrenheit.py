# This program converts from celcius to Fahrenheit taking the celcius value from the user

celcius=float(input("Enter the temperature in Celcius: "))# input function always returns string and hence we need to convert it to number
#To convert String to integer value, we can use "int" function or to convert to float, float function can be used
fahrenheit=((celcius*9)/5)+32
print("The temperature is ",fahrenheit," degrees Fahrenheit.")
if fahrenheit<32 :
       print("It is freezing")
elif fahrenheit<50 :
       print("It is chilly")
elif fahrenheit<90:
       print("It is OK")
else :
       print("It is hot")

