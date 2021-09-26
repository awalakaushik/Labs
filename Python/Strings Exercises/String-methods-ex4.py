#Strings Functions Exercise 4 (Remove All Spaces)
#Write a function which accepts an input string consisting of alphabetic characters and returns the string with all the spaces removed. Do NOT use any string methods for this problem.

def _remove_spaces_sample_(string):
    out_string = ""
    for x in range(0, len(string)):
        if string[x] != " ":
            out_string = out_string + string[x]
    return out_string
