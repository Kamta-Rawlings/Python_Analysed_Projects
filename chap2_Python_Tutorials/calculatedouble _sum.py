'''
QUESTION
You are given a number x.
For every number from 1 up to x, you must:
Add all the numbers from 1 up to that number,
Then add all those results together.
Finally, print the total.
'''
add = 0
total = 0
num = input('Enter the number you want to do sum: ')
numb = int(num)
for i in range(1, numb + 1):
    # factorial *= i     # compute i! by continuing multiplication
    add += i  # add current factorial to total
    total += add
print(total)

'''
Check the exercise on "looping_calfactsum".
same looping method, just change the multiplication to addition
to get this
'''
