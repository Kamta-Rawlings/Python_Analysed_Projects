'''
Write a program that, given a value x, calculates the value
"X factorial"
'''
factorial = 1
num = input('Enter the number you want to do factorial: ')
numb = int(num)
for i in range(1, numb + 1):
    factorial *= i     # compute i! by continuing multiplication
print(factorial)

'''
The main aim here is to understand the what the question
is and try to loop around it.
'''
