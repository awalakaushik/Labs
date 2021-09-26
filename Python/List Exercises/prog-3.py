#Write a function that accepts a list of integers and returns a new list which is the sorted version of the original list (Original list should not be modified). You may NOT use the built in sort() or sorted() functions. Notice that the original list should not be modified

#performing the below sorting using bubble sort algorithm.. Though it is inefficient, we need to solve it for the sake of problem!

def sort_integer_list(integers_list) :
       newlist=integers_list[:]
       length=0
       for element in newlist :
              length=length+1
       unsorted=True
       while unsorted :
              unsorted=False
              for index in range(0,length-1) :
                     if newlist[index] >newlist[index+1] :
                            temp_var = newlist[index]
                            newlist[index]=newlist[index+1]
                            newlist[index+1]=temp_var
                            unsorted=True
       return newlist
              
