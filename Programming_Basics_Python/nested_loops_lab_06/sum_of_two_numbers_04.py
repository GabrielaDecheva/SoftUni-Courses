start_interval = int(input())
end_interval = int(input())
magic_number = int(input())

combination_counter = 0
flag = False

for x in range(start_interval, end_interval + 1):
    for y in range(start_interval, end_interval + 1):
        combination_counter += 1
        if x + y == magic_number:
            flag = True
            break
    if flag:
        break

if flag:
    print(f'Combination N:{combination_counter} ({x} + {y} = {magic_number})')
else:
    print(f'{combination_counter} combinations - neither equals {magic_number}')