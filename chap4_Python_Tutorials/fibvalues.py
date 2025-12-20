'''
QUESTION FIBONACCI sequence
F(n) = F(n-1) + F(n-2)

Note: If a function asks for input,
Example:
>>> fibonacci_values(7)
[0, 1, 1, 2, 3, 5, 8]

'''


def take_input():
    num = int(input('Enter the num you want to find the fib: '))
    while (num < 0):
        num = int(input('Enter the num you want to find the fib: '))
    return num


def fibonacci_values(num):
    output = []
    first_num = 0
    second_num = 1
    if num == 0:
        output = output.append(first_num)
        return output
    if num == 1:
        output = output.append(second_num)
        return output
    else:
        output.append(first_num)
        output.append(second_num)

    for _ in range(2, num):
        next_num = first_num + second_num
        output.append(next_num)
        first_num = second_num
        second_num = next_num

    return output


num = take_input()
result = fibonacci_values(num)
print(result)

'''
Just know how to solve the problem logically before
doing anything.
'''
