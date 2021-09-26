#Dictionary Exercise 6 (Dictionary of Vowel Count)
#Write a function that takes a string as input argument and returns a dictionary of vowel counts i.e. the keys of this dictionary should be individual vowels and the values should be the total count of those vowels. You should ignore white spaces and they should not be counted as a character. Also note that a small letter vowel is equal to a capital letter vowel.

def vowel_count(string):
    vowel_dic={}
    repstring=string.lower().replace(" ","")
    for char in repstring:
        if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
            chcount=repstring.count(char)
            vowel_dic[char]=chcount
    return vowel_dic