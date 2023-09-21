n = int(input())

total_one = 0
total_two = 0

for _ in range(n):
    current_number = int(input())
    total_one += current_number
    continue
for _ in range(n):
    current_number = int(input())
    total_two += current_number

diff = abs(total_one - total_two)
if total_one == total_two:
    print(f'Yes, sum = {total_one}')
else:
    print(f'No, diff = {diff}')