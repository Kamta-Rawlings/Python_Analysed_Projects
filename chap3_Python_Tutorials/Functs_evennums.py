# def is_even(x):
#     # Call the helper function f to compute x % 2
#     result = f(x)    
#     # The number is even if x % 2 equals 0
#     return result == 0


# def f(y):
#     # Return the remainder when y is divided by 2
#     return y % 2
'''
QUESTION
A note on submitting functions on Dodona
When an exercise on Dodona asks for a function (such as this one), Dodona will automatically call the function with different testcases. It therefore is important that you only define the required function (adding additional functions, if needed). Do not call the function yourself in your code. In particular, asking for input with input() will lead to an error, since Dodona does not provide this input when testing a function.

Your code should for example look like this:
'''


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


'''
Use the "return" statement instead of print
'''
