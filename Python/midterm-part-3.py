#Midterm Exam, Part 3 (Most Divisors)
#(10 points possible)
#Write a function called find_integer_with_most_divisors that accepts a list of integers and returns the integer from the list that has the most divisors. In case of a tie, return the first item that has the most divisors. For example: 

#if the list is:

 #[8, 12, 18, 6]
#In this list, 8 has four divisors which are: [1,2,4,8] ; 12 has six divisors which are: [1,2,3,4,6,12]; 18 has six divisors which are: [1,2,3,6,9,18] ; and 6 has four divisors which are: [1,2,3,6]. Notice that both 12 and 18 are tied for maximum number of divisors (both have 6 divisors). Your function should return the first item with maximum numer of divisors; so it should return:
 #12


def find_integer_with_most_dividors(integer_list) :
       divisorcount=[]
       for integer in integer_list :
              count=0
              for x in range(1,integer+1) :
                     if (integer%x)==0 :
                            count+=1
              divisorcount.append(count)
       max_value=max(divisorcount)
       max_index=divisorcount.index(max_value)
       return integer_list[max_index]
