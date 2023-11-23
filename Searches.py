from random import randint

def linear_search(search_list, search_item):
    '''
        Does a search and returns True if the item is found
        Parameters: 
        search_list (list): Any list of items
        search_item (any): Object that you are looking for
    
        Returns: 
        boolean: True if item found, else False
    '''

    #Iterate through the list
    length = len(search_list)
    for i in range(length):
        if search_item == search_list[i]:
            return True
    return False
        

test_list = [1,2,3,4,5,6,7,8,8,9,9,9,9,9,10]
this_search_item = randint(1,18)
print("Searching for: ", this_search_item)
print("Linear search: ", linear_search(test_list, this_search_item))
#print("Binary search: ", recursive_binary_search(test_list, this_search_item))
