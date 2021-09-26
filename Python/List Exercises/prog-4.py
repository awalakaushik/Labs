#LIST MANIPULATION EXERCISE 4 (EXTENDING AND SORTING)
#Write a function that accepts two lists both of which contain integers and returns a new list which contains all the elements from both lists sorted in descending order. Your new list should include duplicate elements if they exist. Do NOT use the built in sort() or sorted() methods.

# performing the sorting in descending order using the merge sort algorithm as it is mentioned that duplicates in the list shouldn't be displayed

def merge_sort_integer_list(a, b):
    a.extend(b)
    # Create a new list
    new_list = []
    # Loop until a becomes empty
    while a:
        # set an arbitrary element as the minimum
        # in this case we chose the first index
        maximum = a[0]
        # loop through the list and
        # find the element that is smallest
        for element in a:
            if element > maximum:
                maximum = element
        # append the smallest element to the new list
        new_list.append(maximum)
        # now remove that smallest element from the original list
        a.remove(maximum)
    # Ultimately a will become empty
    # and the loop will end
    # now return the new list
    return new_list
