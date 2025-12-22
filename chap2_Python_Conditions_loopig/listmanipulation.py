'''
Take in 5 numbers from the users.
Add them to a list and write a loop that prints out each
of the numbers and their squares on a separate line.
The sum of the original numbers and the product of their
squares should be written out at the bottom of the numbers.
Refer to the example below:
12 144
10 100
32 1024
3 9
66 4356
sum of numbers: 123
product of squares: 578086502400
'''
# i = 0
sum_num = 0
prod = 1
count = 0
nums = []
while count < 5:
    # for i in range(1,6):
    digits = input('Enter five numbers of your choice: ')
    nums.append(digits)
    count = count + 1

# print(*nums)

for i in range(5):
    number = int(nums[i])
    square = number * number
    print(f'{nums[i]} {square}')

# for j in nums:
#     sum_num += j

for j in nums:
    sum_num += int(j)
    prod *= int(j) * int(j)

print(f'sum of numbers: {sum_num}')
print(f'product of squares: {prod}')
# print()
# print(nums[0])

# for _ in range(1, 6):
#     digits = input('Enter five numbers of your choice: ')
#     nums.append(digits)
'''
Just try to look at how loop works and understand the question
to loop through.
'''
