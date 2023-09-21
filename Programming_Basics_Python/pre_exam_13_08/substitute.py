k = int(input())
l = int(input())
m = int(input())
n = int(input())

counter_substitute = 0
flag = False

for first_num_one in range(k, 8 + 1):
    for first_num_two in range(9, l - 1, -1):
        for second_num_one in range(m, 8 + 1):
            for second_num_two in range(9, n - 1, -1):
                if first_num_one % 2 == 0 and second_num_one % 2 == 0 and first_num_two % 2 and second_num_two % 2:
                    if first_num_one == second_num_one and first_num_two == second_num_two:
                        print(f'Cannot change the same player.')
                    else:
                        print(f'{first_num_one}{first_num_two} - {second_num_one}{second_num_two}')
                        counter_substitute += 1
                if counter_substitute == 6:
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
    if flag:
        break


