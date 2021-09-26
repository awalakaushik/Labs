#Midterm Exam, Part 9 (GCD)
#(10 points possible)
#Write a function named find_gcd that accepts a list of positive integers and returns their greatest common divisor (GCD). Your function should return 1 as the GCD if there are no common factors between the integers. Here are some examples: 

#if the list was

#[12, 24, 6, 18]
#then your function should return the GCD:
#6
#if the list was
#[3, 5, 9, 11, 13]
#then your function should return their GCD:
#1
from fractions import gcd
from functools import reduce
def find_gcd(some_list) :
       return reduce(lambda x,y: gcd(x,y), some_list)
