'''
Write a script that inputs a
five digit integer from the user.
Separate the number into its individual digits.
Print the separated digits with a single space between each in a single line.
Assume that the user always enters the
correct number of digits. [Hint: Use both the floor division and
remainder operations to separate the digits.] Refer the example below:
'''
num = int(input("Enter five digits: "))
d1 = num // 10000
d2 = (num % 10000) // 1000
d3 = (num % 1000) // 100
d4 = (num % 100) // 10
d5 = (num % 10)
print(f'{d1} {d2} {d3} {d4} {d5}')
# Solution2
# num = input("Enter five digits: ")
# print(*num)

'''
You can use
many approaches here but the question
mentioned to use the floor and mode. However if you are to use
"*num", which is used to unpack strings. (Solution2)
or just use the floor "//" which gives the whole number and eliminates
the remainder
while mode "%" gives us the remainder
'''
