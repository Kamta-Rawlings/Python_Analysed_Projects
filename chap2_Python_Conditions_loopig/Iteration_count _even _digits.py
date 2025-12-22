'''
QUESTION
Write a program that counts the number of
even digits in a given number.
Input
A single line containing an integer X > 0
Output
The number of even digits in the given number.
'''
count = 0
even = []
num = input('Enter the integer, you want to check: ')
# numb = int(num)
for i in num:
    # print(i)
    digit = int(i)
    if digit % 2 == 0:
        count += 1
        even.append(i)
print(count)

'''
This is the last exercise of this chapter.You will be fine
'''

# print(4 % 2)
