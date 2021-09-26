#Dictionary Exercise 7 (Dictionary of Word Count)
#Write a function that takes a string of words as input argument and returns a dictionary of word counts. The keys of this dictionary should be the unique words and the values should be the total count of those words. Assume that characters are not case sensitive. For example if the input string is :

#"I am tall when I am young and I am short when I am old" 
#Then the output should be:
#{'short': 1, 'young': 1, 'am': 4, 'when': 2, 'tall': 1, 'i': 4, 'and': 1, 'old': 1}

def word_count(wordstring):
    word_dic={}
    string=wordstring.lower().split()
    for word in string:
        word_dic[word]=string.count(word)
    return word_dic