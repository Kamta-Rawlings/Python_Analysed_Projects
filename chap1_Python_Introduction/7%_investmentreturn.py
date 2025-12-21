'''
QUESTION
Some investment advisors say that it’s
reasonable to expect a 7% return over the long term in the stock market.
Take in an amount to be invested from the user and calculate how much money
you’ll have after 10, 20 and 30 years. Use the following formula
for determining these amounts:

where
p is the original amount invested (i.e., the principal of $1000),
r is the annual rate of return (7%),
n is the number of years (10, 20 or 30) and
a is the amount on deposit at the end of the nth year.

Print out the resultant values as shown in the example below, you can
ignore everything after the decimal point:
'''

p = int(input('Enter an amount to be invested: '))
r = 0.07
n1 = 10
n2 = 20
n3 = 30
a1 = int(p * (1 + r) ** n1)
a2 = int(p * (1 + r) ** n2)
a3 = int(p * (1 + r) ** n3)
print(f'10 years = {a1}\n20 years = {a2}\n30 years = {a3}')

'''
The most important thing to learn here is how to
use to the power sign "**"
'''
