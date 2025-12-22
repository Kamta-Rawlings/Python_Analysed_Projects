'''
QUESTION
In Arithmetic_min_max.py, you wrote a script that input three integers,
then displayed the sum, average, product, smallest and largest
of those values. Reimplement your script with a loop that inputs four integers.
'''
num1 = int(input('Enter the first interger: '))
num2 = int(input('Enter the second interger: '))
num3 = int(input('Enter the third interger: '))
num4 = int(input('Enter the fourth interger: '))
sum_num = num1 + num2 + num3 + num4
average = sum_num / 4
product = num1 * num2 * num3 * num4

smallest = num1
if num2 < smallest:
    smallest = num2
if num3 < smallest:
    smallest = num3
if num4 < smallest:
    smallest = num4


largest = num1
if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3
if num4 > largest:
    largest = num4

print(f'sum = {sum_num}\naverage = {average}\nproduct = {product}\
\nsmallest = {smallest}\nlargest = {largest}')

'''
Donot over complicate things, same exercise. Just assign a num as
the smallest or largest and then do the comparison.

'''
