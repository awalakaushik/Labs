#Write a function that finds the magnitude of a given vector.
#The magnitude of a vector is the square root of sum of squares of all the components of the
#vector. Your input for this function will be
#a (vector with x,y,z components) 1 dimensional list containing 3 integers.
#For example if the input list is:
#vector = [2, 3, -4]
#Then you should return the magnitude (as a floating point number) of this vector:
#5.385164807134504

#function to find the sum of squares of all components

#def sum_of_squares(list_of_components) :
#       sum=0
 #      for component in list_of_components :
 #             sum += component**2
  #     return sum

#function to find the square root of the sum of squares of components

#def square_root_of_sum_of_squares(sum) :
  #     guess=sum/2
   #    accuracy=0.00000001
     #  while abs(sum-(guess**2))>accuracy :
       #       guess = (guess+(sum/guess))/2
       #return guess

#main program
#vector=[2,3,-4]
#sum=sum_of_squares(vector)
#magnitude=square_root_of_sum_of_squares(sum)
#print(magnitude)


# Alternate solution
def magnitude_of_vector(vector) :
       x=vector[0]
       y=vector[1]
       z=vector[2]
       magnitude=((x**2)**(y**2)**(z**2))**(1/2)
       return magnitude
#main program
vector=[2,3,-4]
magnitude=magnitude_of_vector(vector)
print(magnitude)







