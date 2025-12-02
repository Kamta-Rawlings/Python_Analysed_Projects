'''
QUESTION
Write a program that, given a value x and y,
write a matrix with y rows and x columns containing
the numbers from 1 to x * y.
OUTPUT
1 2 3 4 5 6 7
8 9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31 32 33 34 35
'''

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
while x < 0 or y < 0:
    x = int(input("Enter the value of xcolumns again: "))
    y = int(input("Enter the value of yrows again: "))
# end = x * y
num = 0
for _ in range(y):
    for _ in range(x):
        num += 1
        print(num, end=' ')
    print()

'''
You need first know how matrices work.
Then we loop through the first loop y, then x times.
After looping, 1 is added each time and the num is being printed.
'''
