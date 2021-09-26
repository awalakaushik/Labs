#LIST SLICING EXERCISE 3 (EVERY OTHER ELEMENT)  
#Write a function that accepts a list as input and returns a new list which includes every odd element in the original list. Keep the first element, i.e. input_list[0]. For example if:

#input_list = ["we", "love", "python", "so","much"]
#then your function should return a list such as:
#['we', 'python', 'much']

def every_other_element(sample_list) :
    newlist=[]
    sample_list_length=len(sample_list)
    newlist.append(sample_list[0])
    for x in range(1,sample_list_length) :
        if x%2 == 0 :
            newlist.append(sample_list[x])
    return newlist
