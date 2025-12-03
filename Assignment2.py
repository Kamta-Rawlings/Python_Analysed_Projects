'''
QUESTION
The Fibonacci sequence is a sequence
of numbers where each term is the sum of the \
two preceding ones, starting with 0 and 1:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, …
We can generalize this sequence by choosing any two
starting values a and b, with the condition that:
a ≤ b
For example:
If a = 0 and b = 1, we get the standard
Fibonacci sequence:
0, 1, 1, 2, 3, 5, 8, …

If a = 4 and b = 20, we get the sequence:
4, 20, 24, 44, 68, 112, 180, 292, …

We denote this generalized sequence by fibo(a, b).

Your Task

Write a program that:

Step 1 — Input starting values

Reads two positive integers a and b
(only a is allowed to be 0, and a ≤ b must hold).

Step 2 — Input a sequence S
Then read a sequence of non-zero integers
(positive or negative)
until the user enters 0, which ends the input.

This sequence is called S.

Step 3 — Output

Your program must print:

All values from S (excluding the final 0)
that appear in fibo(a, b)

In the same order they were entered

Separated by a comma and a space

Followed by the total number of valid values printed

Special Cases

If S is empty (the user enters 0 immediately), output:

No values given.
If S is non-empty, but none of its values
appear in fibo(a, b), output:

No valid values.
'''


def accept_input():
    first_num = int(input('Enter the first number of the sequence: '))
    second_num = int(input('Enter the second number of the sequence: '))
    while not (0 <= first_num <= second_num and 0 < second_num):
        first_num = int(input('Enter the correct first number \
of the sequence: '))
        second_num = int(input('Enter the correct second number \
of the sequence: '))
    return first_num, second_num


def store_sequence():
    S = []
    while True:
        seq = int(input('Enter the sequence you want to store \
and end with a 0: '))
        if seq == 0:
            break
        S.append(seq)
    #         print(S)
    return S
    # print(S)


def max_num(firstnum, secondnum, *sequence):
    if len(sequence) == 0:
        return max(firstnum, secondnum)
    return max(firstnum, secondnum, *sequence)


def fibonacci(firstnum, secondnum, fibend):
    fib_sequence = [firstnum, secondnum]
    for _ in range(fibend):
        newnum = firstnum + secondnum
        firstnum = secondnum
        secondnum = newnum
        if newnum > fibend:
            break
        fib_sequence.append(newnum)
    return fib_sequence


def result(sequence):
    count = 0
    output_valid = []
    for num in sequence:
        if num in fib_seq:
            output_valid.append(num)
            count = count + 1

    if len(sequence) == 0:
        print("No values given")
    elif output_valid:
        print(f'{count} valid values: ', end="")
        print(*output_valid, sep=", ")
        # print(f'{count} valid values: ',  *output_valid, sep=",")
        # print(count)
    else:
        print('No valid values')


# --Main Program --#
firstnum, secondnum = accept_input()
sequence = store_sequence()
fibend = max_num(firstnum, secondnum, *sequence)
fib_seq = fibonacci(firstnum, secondnum, fibend)
result(sequence)


'''
Here, we need to learn how to use functions
and use all of the knowledge to build this exercise and this
requires critical thinking
'''
