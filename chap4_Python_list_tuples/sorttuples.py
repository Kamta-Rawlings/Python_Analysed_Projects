'''
Write a function `sort_tuple(t)’ that sorts
a tuple of tuples based on the first value in
each sub-tuple.
Consider using lambda functions in your solution.
'''

# def sort_tuple(t):
#     sorted_list = list(t)

#     for i in range(len(sorted_list)):
#         for j in range(i + 1, len(sorted_list)):
#             if sorted_list[i][0] > sorted_list[j][0]:
#                 sorted_list[i], sorted_list[j] = sorted_list[j],
# sorted_list[i]

#     return tuple(sorted_list)


def sort_tuple(t):
    sorted_list = sorted(t)
    return tuple(sorted_list)


'''
just use sort here,the commented code works well
use "return tuple" to return the tuple
'''
