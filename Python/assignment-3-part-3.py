#Part 3: Find a word in a crossword
#(40 points possible)
#Write a function named capitalize_word_in_crossword that accepts a 2-dimensional list of characters (like a crossword puzzle) and a string (word) as input arguments. This function searches the rows and columns of the 2d list to find a match for the word. If a match is found, this functions capitalizes the matched characters in 2-dimensional list and returns the list. If no match is found, this function simply returns the origianl 2-dimensional list with no modification.

#Example 1: If the function is called as shown below:
       #crosswords=[['s','d','o','g'],['c','u','c','m'],['a','x','a','t'],['t','e','t','k']]
       #word='cat'
       #capitalize_word_in_crossword(crosswords,word)
#then your function should return:
  #[['s','d','o','g'],['C','u','c','m'],['A','x','a','t'],['T','e','t','k']]
#Notice that the above list is a representation for a 2-dimensional crossword puzzle as shown below.
#s	d	o	g
#C	u	c	m
#A	x	a	t
#T	e	t	k Example 2: if the function is called as shown below:
       #crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
       #word='cat'
       #capitalize_word_in_crossword(crosswords,word)
#then your function should return:
  #[['s','d','o','g'],['c','u','c','m'],['a','C','A','T'],['t','e','t','k']]
#Notice that the above list is a representation for a 2-dimensional crossword puzzle as shown below.
#s	d	o	g
#c	u	c	m
#a	C	A	T
#t	e	t	k Note: If both a horizontal and a vertical match is found then only select the horizontal match. For example, in the above case there is a horizontal match starting at [2,1] and there is also a veritcal match starting at [1,0]. Notice that only the characters in the horizontal match should be capitalized in the returned list.
#Hint: You should use the functions that you developed in part 1 and part 2 as helper functions for part 3.


#horizontal match function
def find_word_horizontal(crosswords,word):
       lrow=len(crosswords)
       lcol=len(crosswords[0])
       for i in range(0,lrow):
              for j in range(0,lcol):
                     if j+len(word)<=lcol:
                            match=crosswords[i][j]
                            for l in range(1,len(word)):
                                   match+=crosswords[i][j+l]
                            if word==match:
                                   return [i,j]
       return

#vertical match function
def find_word_vertical(crosswords,word):
       lrow=len(crosswords)
       lcol=len(crosswords[0])
       for col in range(0,lcol):
              for row in range(0,lrow):
                     if row+len(word)<=lrow:
                            match=crosswords[row][col]
                            for l in range(1,len(word)):
                                   match+=crosswords[row+l][col]
                            if word==match:
                                   return [row,col]
       return

#function to find a match and capitalize the word found and return the 2D list

def capitalize_word_in_crossword(crosswords,word):
       horizontal_match=find_word_horizontal(crosswords,word)
       vertical_match=find_word_vertical(crosswords,word)
       if vertical_match!=None and horizontal_match!=None:
              row_match=horizontal_match[0]
              col_match=horizontal_match[1]
              for i in range(0,len(word)):
                     crosswords[row_match][col_match+i]=crosswords[row_match][col_match+i].upper()
              return crosswords       
       elif vertical_match!=None:
              row_match=vertical_match[0]
              col_match=vertical_match[1]
              for i in range(0,len(word)):
                     crosswords[row_match+i][col_match]=crosswords[row_match+i][col_match].upper()
              return crosswords
       elif horizontal_match!=None:
              row_match=horizontal_match[0]
              col_match=horizontal_match[1]
              for i in range(0,len(word)):
                     crosswords[row_match][col_match+i]=crosswords[row_match][col_match+i].upper()
              return crosswords
       else:
              return crosswords
       
#main
print(capitalize_word_in_crossword([['s','d','o','g'],['c','u','c','m'],['a','x','a','t'],['t','e','t','k']],'bat'))
              
              