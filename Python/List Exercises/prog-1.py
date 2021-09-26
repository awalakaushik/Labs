#LIST MANIPULATION EXERCISE 1 (UPDATING A LIST)  
#Write a function that accepts a list and a string and returns the list such that the second through the fourth element (index 1 through 3 both inclusive) in the input list are replaced by the input string. For example:

#input_list = ["Isha", "Chandoygya", "Sri Vasya", "Mandukya", "Sri"]
#input_string = "Brahman" 
#Then, your function should return a list such as:
#['Isha', 'Brahman', 'Brahman', 'Brahman', 'Sri']

def replace_list_with_input_string(sample_list,input_string) :
       for x in range(1,4) :
              sample_list[x]=input_string
       return sample_list
