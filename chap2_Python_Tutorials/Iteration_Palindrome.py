'''
A palindrome is a sequence of characters which reads
the same backward as forward. An example of a palindrome
is “redivider”. Notice that taco cat” is not a palidrome
as its reverse equals “tac ocat”. Also, “Bob” is not a palindrome.
Write a program that checks if a given string is a palindrome.

Can you do it without first mirroring the original input
(or changing or using any other string variable besides)?

Input
A nonempty string
on a single line.

Output
If the given string is
a palindrome, the output should say “X is a palindrome”,
where X is the given string. If not, the output should say
“X is not a palindrome”.

Example
input:
word
output:
word is not a palindrome
input:
redivider

'''
s = input('Enter the string you want to check for palindrome: ')
reverse_s = s[::-1]
if s == reverse_s:
    print(f'{s} is a palindrome')
else:
    print(f'{s} is not a palindrome')

'''
Basically you need to take the string from the user
then you do a reverse string. Then you can compare if the reverse
and the string taken are same.Then print the required output.
'''
