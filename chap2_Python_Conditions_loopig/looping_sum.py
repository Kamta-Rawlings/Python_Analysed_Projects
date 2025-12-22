'''
Write a program that, given a value,
calculates the the summation from 1 till the number
For example 6 gives 21
'''
x = int(input('Enter the number you want to sum: '))
sum_num = 0
for i in range(1, x + 1):
    sum_num = i + sum_num
print(sum_num)
'''
Firstly, know how range works, later initialize a variable to 0
and later interate and start adding it.
'''
