'''
What is the output of the following program?
In the coding space, enter your answers instead
of/before the comments. You can delete the comments if required.
'''

x = 7


def f(g):
    h = g * x
    return h


def g(x):
    return 3


print(f(g(f(g(100)))))

'''
OUTPUT
21
Look at the 2 functions especiallyy the one under, it will 
always return 3. so g(x)=3, and x=7 , so 7 * 3 = 21.
'''
