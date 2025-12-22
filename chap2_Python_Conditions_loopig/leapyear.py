'''
QUESTION
A leap year is a year with an extra day in February.
More formally,
a year is a leap year whenever the following rule applies:
the year is divisible by 4, unless it is divisible by 100
and not by 400. Leap years include 2000 and 2016, but 1900
is not a leap year. Write a program that checks if a given year is a leap year.
Input
A single line containing a year.
Output
If the given year is a leap year, the output should say
“X is a leap year”, where X is the given year.
If not, the output should say “X is not a leap year”.
'''
year = int(input("Enter the year you want to check: "))
if (year % 4 == 0 and year % 100 == 0 and year % 400 == 0) or \
      (year % 4 == 0 and year % 100 != 0):
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')

# if (year % 4 == 0) or year % 100 == 0 and year % 400 != 0:
#     print('This is not a leap year')
# if (year % 4 == 0) and year % 400 == 0:
#     print('This is a leap year')

'''
The main aim here is understand what
we used mode, brackets ,
and or and most od the operations in python

'''
