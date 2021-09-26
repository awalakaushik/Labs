#Write a function that takes a list of words as an input argument and returns True if the list is sorted and returns False otherwise.

def is_sorted_list(word_list) :
       word_list_copy=word_list[:]
       word_list.sort()
       if word_list_copy == word_list :
              return True
       else :
              return False
