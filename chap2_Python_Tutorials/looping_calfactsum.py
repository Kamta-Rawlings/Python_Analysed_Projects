'''
Write a program that asks the user for a positive integer x.
Then compute the value:
In other words, your program
must calculate the sum of all factorials from 1! up to x!.
Finally, print the result.

Example:
If the user enters 7, your program should compute:
1! + 2! + 3! + 4! + 5! + 6! + 7! = 5913
'''
factorial = 1
total = 0
num = input('Enter the number you want to do factorial: ')
numb = int(num)
for i in range(1, numb + 1):
    factorial *= i     # compute i! by continuing multiplication
    total += factorial   # add current factorial to total
print(factorial)

'''
Most importantly, understand what you are looking for.
This question is very tricky because ,
you have to just keep adding eachh factorial to the total.

'''
