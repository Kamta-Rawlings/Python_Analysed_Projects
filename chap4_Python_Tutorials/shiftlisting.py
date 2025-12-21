'''
QUESTION
Write a function shift(l, n) that accepts a list
l and a number n, and returns the list obtained by
shifting the elements in the list n places to the right
(left) when n is positive (negative). Use wrap-around: if an element
is shifted beyond the end of the list, then
continue to shift starting at the beginning of the list.
example:
>>> shift([1, 2, 3, 4, 5], 2)
[4, 5, 1, 2, 3]
>>> shift([1, 2, 3, 4, 5], -2)
[3, 4, 5, 1, 2]


'''


def shift(l, n):
    # If the list is empty, return it unchanged
    if len(l) == 0:
        return l

    # Reduce n so it is within the list length
    n = n % len(l)

    # Split and rejoin the list
    return l[-n:] + l[:-n]


'''
Learn Python slicing well and
most importantly understand what the question ask us
'''
