#Midterm Exam, Part 7 (Pattern Sum)
#(10 points possible)
#Write a function called pattern_sum that receives two single digit positive integers, (k and m) as parameters and calculates and returns the total sum as: 
#k + kk + kkk + .... (the last number in the squence should have m digits) 
#For example if the two integers are:

#(4, 5)
#Your function should return the total sum of: 
#4 + 44 + 444 + 4444 + 44444 
#Notice the last number in this sequence has 5 digits. The return value should be:
#49380
#if the two integers are:
#(5, 3)
#Your function should return the total sum of: 
#5 + 55 + 555 
#Notice the last numebr in this squence has 3 digits. The return value should be:
#615

def pattern_sum(a, b):
        pattern_list=[]
        pattern_list.append(a)
        pattern_num=a
        for x in range(2,b+1) :
            pattern_num=pattern_num*10+a
            pattern_list.append(pattern_num)
        sum=0
        for pnum in pattern_list :
            sum+=pnum
        return sum
