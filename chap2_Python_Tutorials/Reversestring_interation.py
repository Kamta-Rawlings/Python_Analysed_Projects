'''
QUESTION
Write a program
that outputs the reverse of a given string.
For example Bob
gives boB
'''
s = input("Please enter the string you want to reverse: ")
# reversed_s = s[::-1]
i = len(s) - 1
reversestring = []

for _ in s:
    reversestring.append(s[i])
    i -= 1
print("".join(reversestring))

'''
learn how to use string slicing
s[start:stop:step] to do thuis shorter but if you want
to learn looping, intialize an empty string to store what we wil
remove and store in it. we use "i = len(s)-1" so we can iterate through
the string.
'''
