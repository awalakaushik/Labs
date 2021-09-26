#Functions:
#Nothing goes in, nothing comes out

def display_message():
    print("****   PYTHON IS GREAT   ****")
    print("=============================")
    
# Main Program #
print("Function type: Nothing goes in, nothing comes out")
radius = 5
print("The radius of the circle is: ", radius)
display_message()    # The function call 

circumference = 2*3.14*radius
print("The circumference of the circle is:", circumference)
display_message()    # The function call 
##############################################################
#Nothing goes in, something comes out
import random

def report_random():
    my_number = random.randint(20, 100)
    return my_number

# Main Program #
print("Function type: Nothing goes in, something comes out")
a = report_random()    # return a random int and assign it to a
print("a is equal to ", a)
b = report_random()    # return a random int and assign it to b
print("b is equal to ", b)
c = report_random()    # return a random int and assign it to c
print("c is equal to ", c)


##########################################################

#Function type: Something goes in, nothing comes out

def calculate_area(length, breadth):
    area = length * breadth
    perimeter = 2*length + 2*breadth
    print("area is equal to", area)
    print("perimeter is equal to", perimeter)

# Main Program #
print("Function type: Something goes in, nothing comes out")
calculate_area(10, 20)

############################################################

#Function type: Something goes in, something comes out

def calculate_area(length, breadth):
    area = length * breadth
    perimeter = 2*length + 2*breadth
    my_result = [area, perimeter]    # put results in a list
    return my_result                 # return the list

# Main Program #
print("Function type: Something goes in, nothing comes out")
my_list = calculate_area(10, 20) # two arguments are supplied 
print("The resulting list looks like:", my_list)


