#Part 3: Spelling corrector
#(40 points possible)
#Write a function named spelling_corrector that accepts two arguments. The first argument is a sentence (string) and the second argument is a list of words (correct_spells). Your function should check each word in the input string against all the words in the correct_spells list and return a string such that:

#If a word in the original sentence matches exactly with a word in the correct_spells then the word is not modified and it should be directly copied to the output string.
#if a word in the sentence can match a word in the correct_spells list by replacing, inserting, or deleting a single character, then that word should be replaced by the correct word in the correct_spelled list.
#If neither of the two previous conditions is true, then the word in the original string should not be modified and should be directly copied to the output string.
#Notes:
#Do not spell check one or two letter words (copy them directly to the output string).
#In case of a tie use the first word from the correct_spelled list.
#Ignore capitalization, i.e. consider capital letters to be the same as lower case letters.
#All characters in the output string should all be in lower case letters.
#Assume that the input string only includes alphabetic characters and spaces. (a-z and A-Z)
#Remove extra spaces between the words.
#Remove spaces at the start and end of the output string.
#Examples:
#Sentence (str)	                          correct_spells (list)	                                  Function return (str)
#Thes is the Firs cas	          ['that','first','case','car']	                                  thes is the first case
#programing is fan and eesy          ['programming','this','fun','easy','book' ]     programming is fun and easy
#Thes is vary essy	                          ['this', 'is', 'very', 'very', 'easy']	                  this is very easy
#Wee lpve Pythen	                          ['we', 'Live', 'In', 'Python']	                  we live python
#Notice:
#In the first example 'thes' is not replaced with anything.
#In the first example both 'case' and 'car' could replace the 'cas' in the original sentence, but 'case' is selected because it was encountered first.
#Please notice that this assignment is only an exercise and a real spell checker requires more functionalities.
#Hint: You should use the functions that you developed in part 1 and part 2 to help you solve this problem.

#function to find the single insertion or deletion
def single_insert_or_delete(s1,s2):
       alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
       if s2.lower().strip() == s1.lower().strip():
              return 0
       elif s2.lower().strip()!=s1.lower().strip():
              for alphabet in alphabets:
                     if alphabet+s1.lower().strip()==s2.lower().strip() or s1.lower().strip()+alphabet==s2.lower().strip():
                            return 1
              for index in range(0,len(s1)):
                     if(s1[:index]+s1[index+1:]).lower().strip()==s2.lower().strip():
                            return 1
                     for alphabet in alphabets:
                            if (s1[:index]+alphabet+s1[index:]).lower().strip()==s2.lower().strip():
                                   #print((s1[:index]+alphabet+s1[index:]).lower())
                                   return 1
                            elif (s2[:index]+alphabet+s2[index:]).lower().strip()==s1.lower().strip():
                                   #print((s2[:index]+alphabet+s2[index:]).lower())
                                   return 1
                            elif (s1.replace(s1[index],alphabet,1)).lower().strip()==s2.lower().strip():
                                 return 1
                            elif (s1[0:index]+s1[index-1:index].replace(s1[index],alphabet,1)+s1[index+1:].lower().strip())==s2.lower().strip():
                                   return 1
              return 2
def spelling_corrector(sentence,correct_spell_list):
       sentence_list=sentence.lower().split(" ")
       output_string=""
       output_str_list=[]
       for word in sentence_list:
              eqval=0
              if len(word)>2 and word.lower().strip() not in correct_spell_list:
                     for list_word in correct_spell_list:
                            eqval=single_insert_or_delete(word.strip(),list_word.lower())
                            #print(word,list_word.lower(),eqval,end="\n")
                            if eqval==1 or eqval==0:
                                   break;
                     if eqval==2:
                            output_str_list.append(word.lower().strip())
                     elif eqval==1:
                            output_str_list.append(list_word.lower().strip())
                     elif eqval==0:
                            output_str_list.append(word.lower().strip())
              else:
                     output_str_list.append(word.lower().strip())
              while "" in output_str_list:
                     output_str_list.remove("")
       return " ".join(output_str_list).strip()
#main program
print(spelling_corrector("Thes is the Firs cas",['that','first','case','car']))
print(spelling_corrector("programing   is fan and eesy",['programming','this','fun','easy','book']))
print(spelling_corrector("Thes is vary essy",['this','is','very','very','easy']))
print(spelling_corrector("Wee lpve Pythen",['we','Live','In','Python']))
print(spelling_corrector("Asignment three xample inpu ",['Assignmen', 'tree', 'three', 'example', 'output', 'input']))
