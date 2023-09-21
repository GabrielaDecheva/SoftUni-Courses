number = int(input())

even = 0
odd = 0

for i in range(number):
    current_number = int(input())
    if i % 2 == 0:
        even += current_number
    else:
        odd += current_number

diff = abs(even - odd)

if even == odd:
    print('Yes')
    print(f'Sum = {even}')
else:
    print('No')
    print(f'Diff = {diff}')