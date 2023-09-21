n = int(input())

current_num = 1
current_bigger_than_n = False

for row in range(1, n + 1):
    for col in range(1, row + 1):
        if current_num > n:
            current_bigger_than_n = True
            break
        print(current_num, end=' ')
        current_num += 1
    print()
    if current_bigger_than_n:
        break