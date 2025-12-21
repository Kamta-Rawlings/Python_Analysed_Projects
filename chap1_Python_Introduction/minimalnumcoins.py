'''
QUESTION
Write a program that writes out how to pay a given
amount of money (in eurocent) with a minimum number of coins
(using coins of 2 or 1 euro, or 50, 20, 10, 5, 2, or 1 eurocent).

Input
The input consists of a single line containing an integer:
the amount of money to be paid (in eurocent).

Output
On a separate line for each type of coin, the number
of coins necessary to pay the requested amount.
'''
amnt = int(input('Enter the amount you want to be paid: '))

coins = [
    (200, "2-euros"),
    (100, "1-euros"),
    (50, "50c-euros"),
    (20, "20c-euros"),
    (10, "10c-euros"),
    (5, "5c-euros"),
    (2, "2c-euros"),
    (1, "1c-euros")
]

for value, label in coins:
    count = amnt // value
    amnt = amnt % value
    # e.g 589 % 200 = 189
    print(f'{label}: {count}')

'''
This is abiot complicated, firstly we take in the number
we want to be paid out,
Then we later create a list of tuples.
We loop through that list and use the floor
method to get the the whole num first then we keep
changing the remainder with the mode function
'''
