'''
QUESTION
sum_tuples(tuple_a, tuple_b, tuple_c)
What should this function do?
It takes three tuples as input

All three tuples have the same length

It adds the elements position by position

It returns one new tuple containing those sums
'''


def sum_tuples(tuple_a, tuple_b, tuple_c):
    result = []

    for i in range(len(tuple_a)):
        total = tuple_a[i] + tuple_b[i] + tuple_c[i]
        result.append(total)

    return tuple(result)


'''
This is the simplest form of this tuple addition.
loop through the len of the first tuple,
add and return the tuple.
'''
