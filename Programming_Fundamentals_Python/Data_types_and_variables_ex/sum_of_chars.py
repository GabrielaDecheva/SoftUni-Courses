n = int(input())
total_sum = 0
for char in range(n):
    current_input = input()
    total_sum += ord(current_input)
print(f'The sum equals: {total_sum}')