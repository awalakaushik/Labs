#Write a program using while loop, which prints the sum of every third numbers from 1 to 1001
#( both 1 and 1001 are included)
#(1 + 4 + 7 + 10 + ....)

start = 1 
end = 1001
sum = 0
while start <= end :
       sum += start
       start += 3
print(sum)
