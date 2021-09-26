#Quiz 5, Part 3
#(20 points possible)
#Write a function named construct_dictionary_from_lists that accepts 3 one dimensional lists and constructs and returns a dictionary as specified below. 
#The first one dimensional list will have n strings which will be the names of some people.
#The second one dimensional list will have n integers which will be the ages that correspond to those people.
#The third one dimensional list will have n integers which will be the scores that correspond to those people.
#Note that if a person has a score of 60 or higher (score >= 60) that means the person passed, if not the person failed.
#Your function should return a dictionary where each key is the name of a person and the value corresponding to that key should be a list containing age, score, 'pass' or 'fail' in the same order as shown in the sample output.
#For example, if the function receives the following lists:

#(["paul", "saul", "steve", "chimpy"], [28, 59, 22, 5], [59, 85, 55, 60])
#then your function should return the dictionary such as:
#{'steve': [22, 55, 'fail'], 'saul': [59, 85, 'pass'], 'paul': [28, 59, 'fail'], 'chimpy': [5, 60, 'pass']}
#Note that the order of the keys of the dictionary does not need to be the same as shown in this sample example.

def construct_dictionary_from_lists(names_list, ages_list, scores_list):
    outputdic={}
    scorestr=""
    for name in names_list:
        if scores_list[names_list.index(name)]>=60:
            scorestr="pass"
            age=ages_list[names_list.index(name)]
            score=scores_list[names_list.index(name)]
        else:
            scorestr="fail"
            age=ages_list[names_list.index(name)]
            score=scores_list[names_list.index(name)]            
        outputdic[name]=[age,score,scorestr]
    return outputdic
#main
print(construct_dictionary_from_lists(["paul", "saul", "steve", "chimpy"], [28, 59, 22, 5], [59, 85, 55, 60]))