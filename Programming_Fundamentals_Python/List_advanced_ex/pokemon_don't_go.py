sequence = list(map(int, input().split()))
sum_of_removed_elements = 0
while sequence:
    index = int(input())
    if index < 0:
        deleted_num = sequence[0]
        sequence[0] = sequence[-1]
        for element in range(len(sequence)):
            if sequence[element] <= deleted_num:
                sequence[element] += deleted_num
            else:
                sequence[element] -= deleted_num
        sum_of_removed_elements += deleted_num
    elif index > len(sequence) - 1:
        deleted_num = sequence[-1]
        sequence[-1] = sequence[0]
        for element in range(len(sequence)):
            if sequence[element] <= deleted_num:
                sequence[element] += deleted_num
            else:
                sequence[element] -= deleted_num
        sum_of_removed_elements += deleted_num
    else:
        deleted_num = sequence.pop(index)
        for element in range(len(sequence)):
            if sequence[element] <= deleted_num:
                sequence[element] += deleted_num
            else:
                sequence[element] -= deleted_num
        sum_of_removed_elements += deleted_num

print(sum_of_removed_elements)