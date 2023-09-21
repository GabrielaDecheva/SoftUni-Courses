first_num = int(input())
second_num = int(input())

for i in range(first_num, second_num + 1):
    current_num_str = str(i)

    even_sum = 0
    odd_sum = 0
    for j in range(0, len(current_num_str)):
        digit = int(current_num_str[j])

        if j % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    if even_sum == odd_sum:
        print(current_num_str, end=' ')