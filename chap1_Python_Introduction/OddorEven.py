'''
QUESTION
Get a positive integer from the user using the input
function and determine whether an integer
is odd or even using the if statement.
[Hint: Use the remainder operator. An even number is a
multiple of 2. Any multiple of 2 leaves a remainder of 0 when divided by 2.]

'''
num = int(input("Enter a positive integer: "))
if num % 2 == 0:
    print('even')
else:
    print('odd')

'''
We know any number divisible by 2 without a remainder is even .
We also got introduced to the mode function.
'''
