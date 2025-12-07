'''
QUESTION
Functions - Evaluate following code fragments

'''
x = 7


def f(y):
    if (x < y):
        return g(y)
    else:
        y = x * x
        return y


def g(x):
    return x * 12


y = 1
z1 = f(y)
z2 = f(15)
print(x, y, z1, z2)

'''
This is a mental drill question
Just understand how functions work and try to give the output mentally.
'''
