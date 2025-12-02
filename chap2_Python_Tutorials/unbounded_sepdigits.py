# firstNum = int(input('Enter the first number a of the sequence: '))
# a = [1, 2, 3]
# print(f'{max(a)}')
# newnum = []
# num = input('Enter a long interger: ')
# int_num = int(num)
# a = len(num) - 1
# divisor = 10 ** a
# first_digit = int_num // divisor
# print(divisor)
# for i in range(len(num)):
#     new_digit = int_num % divisor
#     newnum.append(first_digit)
#     num = num % divisor
#     divisor //= 10 # new_len = len(str(new_digit)) - 1
# new_divisor = 10 ** new_len
# first_digit = new_digit // new_divisor
# divisor = divisor // 10
# newnum.append(digits)
# newdivisor = 2 ^ (a - 1)S
# divisor = divisor / newdivisor
# print(*newnum)
# print(*newnum)


#  num = input("Enter a long integer: ")
# newnum = [int(d) for d in num]
# print(*newnum)

'''
In Exercise 1.06, you wrote a script that separated a
five-digit integer into its individual digits and displayed them.
Reimplement your script to use an unbounded loop that in each
iteration “picks off” one digit (left to right)
from a digit of any length using the //
and % operators, then displays that digit as shown below.
example:
34634777 gives
3 4 6 3 4 7 7 7

'''

num = input('Enter a long integer: ')
int_num = int(num)
divisor = 10 ** (len(num) - 1)
newnum = []

for _ in range(len(num)):
    first_digit = int_num // divisor
    newnum.append(first_digit)
    int_num = int_num % divisor
    divisor //= 10

print(*newnum)

'''
The first step is take the
users input as a string(so as to later use (*num)
to unpack the string. we then convert the string
to int and the divisor is also length of the num -1.
We then create an empty list, then loop through the length
and then use ".append" to add the fisrt digit or digits.
and we continue with the remainder
and later we keep reducing the divisor

'''
