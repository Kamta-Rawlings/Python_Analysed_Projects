# write your code here
'''
Write a script that inputs three integers from the user.
Display the sum, average, product, smallest and largest of the numbers.
Print the results in the following format: (example: 4,8,3)
sum = 15
average = 5.0
product = 96
smallest = 3
largest = 8

'''
num1 = int(input('Enter the first interger: '))
num2 = int(input('Enter the second interger: '))
num3 = int(input('Enter the third interger: '))
sum_num = num1 + num2 + num3
average = sum_num / 3
product = num1 * num2 * num3

smallest = num1
if num2 < smallest:
    smallest = num2
elif num3 < smallest:
    smallest = num3

largest = num1
if num2 > largest:
    largest = num2
elif num3 > largest:
    largest = num3

print(f'sum = {sum_num}\naverage = {average}\nproduct = {product}\
\nsmallest = {smallest}\nlargest = {largest}')

'''
The main challenge here is assigning one digit
as the smallest or largest num and later doing the comparison with the if and
elif statements. or you can use "min or max"
'''
