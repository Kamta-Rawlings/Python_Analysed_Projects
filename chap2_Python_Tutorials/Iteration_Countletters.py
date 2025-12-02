'''
QUESTION
Write a program that writes out how many times each
lower case character occurs in a given string.
Input
A nonempty string on a single line.
Output
For each lowercase letter in the alphabet,
one line that shows how many times this letter
occurs in the input string.
'''
letters = "abcdefghijklmnopqrstuvwxyz"
# store = []
# count = 0
s = input("Enter the string you want to count lower letters: ")
for i in letters:
    count = 0
    for j in s:
        if i == j:
            count += 1
    print(f'{i}: {count}')

'''
Try to understand the question properly. And then we intialiaze the
count under the first loop because we want it to be zeero
each time we move to a new letter.
'''
