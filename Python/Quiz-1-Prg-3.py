#Write a program that asks the user for a positive integer between 1 and 7 (Assume that the user may enter any number from 1 to 7 both inclusive) and prints the day of week corresponding to that number in all capital letters. Assume that the day of the week starts from MONDAY. For example: if the user enters:
#2
#then your program should print
#TUESDAY
#if the user enters
#5
#then your program should print
#FRIDAY
#etc. Do NOT use shortcut names for the days of the weeks like "tue" or "fri". The names have to be completely spelled in Capital lettets. Hint: Use a list containing days of the week.
#Pay attention to the spaces. In order to receive proper grade, your output should EXACTLY match the output shown in the sample solution (highlighted in yellow) including spaces and capitalization.

day_of_week=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
user_input=int(input())
print(day_of_week[user_input-1])



#It can also be written as follows!
#user_input=int(input())
#if user_input==1 : print("MONDAY")
#if user_input==2 : print("TUESDAY")
#if user_input==3 : print("WEDNESDAY")
#if user_input==4 : print("THURSDAY")
#if user_input==5 : print("FRIDAY")
#if user_input==6 : print("SATURDAY")
#if user_input==7 : print("SUNDAY")
