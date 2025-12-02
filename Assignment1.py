'''
QUESTION
Write a program that accepts 3 positive integers, a b, c
,and  (of which only "c" can have the value 0), and prints,
for all numbers in the closed interval [a,b] (including both a and b),
the line
i^0 + i^1 + i^2 ....i^c sum j
in which is the value of the sum i^0 + i^1 + i^2 ....i^c
.The values are separated by a single space. You may assume
only valid input is given, i.e., 3 arbitrary integers a,b and c
,with  0 < a <= b and c >= 0

OUTPUT
1 1 1 1 1 1 sum 6
1 2 4 8 16 32 sum 63
1 3 9 27 81 243 sum 364
1 4 16 64 256 1024 sum 1365
'''

# write your code here
# print('Please Enter the first 2 integers such that  0<a<=b. The first   \
# integer is smaller than the second')
a = int(input("Enter the first positive integer: "))
b = int(input("Enter the second positive integer: "))
c = int(input("Enter the third integer(include zero): "))
# while a <= 0 or b <= 0 and c >= 0:
while not (0 < a <= b and c >= 0):
    a = int(input("Please enter a correct 1st positive integer: "))
    b = int(input("Please enter a correct 2nd positive integer: "))
    c = int(input("Please enter a correct 3rd integer(include zero): "))
# print(f'The numbers you have chosen are a: {a} and b: {b} and c: {c}')
sum_num = 0
for i in range(a, b+1):
    for j in range(c+1):
        prod = i ** j
        sum_num += prod
        # sum = sum + prod
        print(f'{prod} ', end='')
    print(f'sum {sum_num}')
    sum_num = 0
'''
The main aim is to identify the solution pattern of this program.
Like doing the mathematics mentally, then try to fit or check if the
solution has a pattern.
We made use of the while statement, not comparison. Moreover
after receiving the users input we use "while"
to force the user to give the correct input. we loop through using "for"
and the "range (a, b+1)" 'the range starts from a to b'.
'''
