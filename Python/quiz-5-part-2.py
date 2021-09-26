#Quiz 5, Part 2
#(20 points possible)
#Write a function named row_maximums that accepts a 2-dimensional list of numbers as parameter and returns a dictionary whose values would be the maximum value of each row and whose keys would be the appropriate strings as specified below. 

#For example if the function receives the following list:

#[[5, 0, 0, 0, 13],
 #[0, 12, 0, 0],
 #[20, 0, 11, 0],
 #[6, 0, 0, 8]] 
#then your function should return the dictionary such as:
#{'row 0 max': 13, 'row 1 max': 12, 'row 3 max': 8, 'row 2 max': 20}
#Notes:
#Everything in the keys is separated by one space and the characters are lower cased.
#The 2-dimensional list may have unequal number of rows and columns.
#The row indicies for the keys should start at 0 and go to n. So your program should work for any number of rows and columns.
#You may not use the built in max() function.

def row_maximums(samplelist):
    outputdic={}
    for row in samplelist:
        rowmax=row[0]
        for item in row:
            if rowmax<item:
                rowmax=item
        outputdic["row "+str(samplelist.index(row))+" max"]=rowmax
    return outputdic