#Write a program which prints the sum of numbers from 1 to 101 ( 1 and 101 are included) that are divisible by 5 (Use while loop)
start=1
end=101
sum=0
while start<=end :
       if start%5 == 0 :
              sum+=start
       start+=1
print(sum)
