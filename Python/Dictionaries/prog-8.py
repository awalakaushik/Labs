#Dictionary Exercise 8 (Numbers To Words)
#Write a function that takes an integer as input argument and returns the integer using words. For example if the input is 4721 then the function should return the string "four seven two one". Note that there should be only one space between the words and they should be all lowercased in the string that you return.

def numinwords(integer):
    intdic={"1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine","0":"zero"}
    outputstr=""
    intstr=str(integer)
    splitstr=list(intstr)
    for num in splitstr:
        outputstr+=intdic[num]+" "
    stripped=outputstr.strip(" ")
    return stripped