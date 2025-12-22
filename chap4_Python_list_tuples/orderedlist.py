'''
Write a function is_ordered(l) that checks whether
a list of numbers is ordered.
Example:
>>> is_ordered([1, 2, 3, 4, 5, 6, 7, 8, 9])
True
'''
# def is_ordered(listnum):
#     for i in range(len(listnum) - 1):
#         # for j in range(i + 1, len(listnum)):
#         if listnum[i] < listnum[i+1]:
#             return True
#     return False


def is_ordered(listnum):
    for i in range(len(listnum) - 1):
        if listnum[i] > listnum[i + 1]:
            return False
    return True


'''
Try to make sure the loop doesnt extend the range
And do the comparison right
'''
