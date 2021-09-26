#Quiz 5, Part 4
#(20 points possible)
#Write a function named one_to_2D which receives an input list and two integers r and c as parameters and returns a new two-dimensional list having r rows and c columns. 

#Note that if the number of elements in the input list is larger than r*c then ignore the extra elements. If the number of elements in the input list is less than r*c then fill the two dimensional list with the keyword None. Hint: The first row should contain the first r elements and so forth ...

def one_to_2D(some_list, r, c):
    min_el_size=r*c
    length=len(some_list)
    el_pos=0
    output_list=[[] for i in range(0,r)]
    if length<min_el_size:
        for i in range(0,r):
            for j in range(0,c):
                if el_pos<length:
                    output_list[i].append(some_list[el_pos])
                    el_pos+=1
                else:
                    el=None
                    output_list[i].append(el)
    else:
        for i in range(0,r):
            for j in range(0,c):
                if el_pos<min_el_size:
                    output_list[i].append(some_list[el_pos])
                    el_pos+=1
                else:
                    el=None
                    output_list[i].append(el)        
    return output_list

#main
print(one_to_2D([1,2,3,4,5,6,7],3,2))