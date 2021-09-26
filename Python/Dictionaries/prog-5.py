#Dictionary Exercise 5 (Dictionary of Letter Count)
#Write a function that takes a string as input argument and returns a dictionary of letter counts i.e. the keys of this dictionary should be individual letters and the values should be the total count of those letters. You should ignore white spaces and they should not be counted as a character. Also note that a small letter character is equal to a capital letter character.

def letter_count(inputstring):
    outputdic={}
    string=inputstring.lower().replace(" ","")
    for alphabet in string:
        lettercount=string.count(alphabet)
        outputdic[alphabet]=lettercount
    return outputdic