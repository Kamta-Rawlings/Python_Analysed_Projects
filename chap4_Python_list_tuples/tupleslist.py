'''
Write a function all_elements(tpl) that converts
a given a tuple into a list. Your function should
return a list containing all
elements that occur in the tuple, in the original order.
Example:
>>> all_elements(("A", "B", "C", "D"))
["A", "B", "C", "D"]

'''


def all_elements(tpl):
    newlist = []

    for item in tpl:
        newlist.append(item)

    return newlist


'''
Just loop through the loop list and store it in an array
'''
