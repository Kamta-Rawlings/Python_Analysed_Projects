'''
Write a function remove_tuple_from_list(the_list, the_tuple)
that modifies and returns the given list by removing
all elements that occur in the given tuple as well
Example:
>>> remove_tuple_from_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], (2, 3, 5, 7))
[1, 4, 6, 8, 9, 10]
'''


def remove_tuple_from_list(the_list, the_tuple):
    newlist = []

    for item in the_list:
        if item not in the_tuple:
            newlist.append(item)

    return newlist


'''
We first check the an item in the list. then check the item is in the tuple
then just ass it in the new list created.
'''
