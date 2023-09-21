import sys

n = int(input())

max_num = -sys.maxsize
sum_nums = 0

for _ in range(n):
    current_num = int(input())
    sum_nums += current_num

    if current_num > max_num:
        max_num = current_num

if max_num == sum_nums - max_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    diff = abs(max_num - (sum_nums - max_num))
    print('No')
    print(f'Diff = {diff}')


