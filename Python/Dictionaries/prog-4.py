#Dictionary Exercise 4 (Value Containing Key)
#Write a function which accepts a dictionary and an integer as input and returns an ascending sorted list of all the keys whose values contain the input value. Note that the keys of this dictionary are strings while the values of this dictionary are 1 Dimensional lists of integers. For example if the input dictionary is:

#sample = {"rabbit" : [1, 2, 3],
          #"kitten" : [2, 2, 6],
          #"lioness": [6, 8, 9]}
#and the input integer is 2 then your function should return:
#[ "kitten", "rabbit",]
#If the input integer is not found then your function should return an empty list.

def ascending_sorted_list(dic,integer):
    keys=dic.keys()
    output_list=[]
    for key in keys:
        if integer in dic[key]:
            output_list.append(key)
    output_list.sort()
    return output_list