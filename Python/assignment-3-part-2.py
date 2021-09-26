#Part 2: Find a word in a crossword (Verical)
#(30 points possible)
#Write a function named find_word_vertical that accepts a 2-dimensional list of characters (like a crossword puzzle) and a string (word) as input arguments. This function searches the columnss of the 2d list to find a match for the word. If a match is found, this functions returns a list containing row index and column index of the start of the match, otherwise it returns the value None (no quotations).

#For example if the function is called as shown below:
       #crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
       #word='cat'
       #find_word_vertical(crosswords,word)
#then your function should return [1,0]
#Notice that the 2d input list represents a 2d crosswords and the starting index of the vertical word 'cat' is [1,0]

#s	d	o	g
#c	u	c	m
#a	c	a	t
#t	e	t	k Note: In case of multiple matches only return the match with lower column index. If you find two matches in the same column then return the match with lower row index.

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

#main
print(find_word_vertical([['s','d','o','g'],['c','u','c','m'],['a','x','a','t'],['t','e','t','k']],'cat'))