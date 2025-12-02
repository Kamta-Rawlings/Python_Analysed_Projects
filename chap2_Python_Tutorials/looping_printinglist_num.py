'''
Write a program that asks for a value x and
writes a monospaced list starting from 1
upto and including the value x. See below
for example
7 gives
1 2 3 4 5 6 7
'''
# write your code here
x = int(input("Enter the range you want to print: "))
y = range(1, x + 1)
print(*y)

'''
We make use of the "range" function here
'''
