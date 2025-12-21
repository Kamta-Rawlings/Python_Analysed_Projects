'''
Write a function is_unique(t)
that checks whether all values in the tuple are unique.
Example:
>>> is_unique((1, 2, 3, 4, 5, 6, 7, 8, 9))
True
'''


def is_unique(listnum):
    for i in range(len(listnum)):
        for j in range(i + 1, len(listnum)):
            if listnum[i] == listnum[j]:
                return False
    return True


'''
Try to understand and use two
range works and loop through then just compare the two
'''
