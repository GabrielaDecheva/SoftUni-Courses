def is_invalid_index(current_index, input_sequence):
    return (
        current_index < 0
        or current_index > len(input_sequence) - 1
    )


def handle_invalid_index(current_index, input_sequence,):
    removed_elements = 0
    if current_index < 0:
        deleted_num = input_sequence[0]
        input_sequence[0] = input_sequence[-1]
        for element in range(len(input_sequence)):
            if input_sequence[element] <= deleted_num:
                input_sequence[element] += deleted_num
            else:
                input_sequence[element] -= deleted_num
        removed_elements += deleted_num
    elif current_index > len(input_sequence) - 1:
        deleted_num = input_sequence[-1]
        input_sequence[-1] = input_sequence[0]
        for element in range(len(input_sequence)):
            if input_sequence[element] <= deleted_num:
                input_sequence[element] += deleted_num
            else:
                input_sequence[element] -= deleted_num
        removed_elements += deleted_num
    return removed_elements


def handle_valid_index(current_index, input_sequence,):
    removed_elements = 0
    deleted_num = input_sequence.pop(current_index)
    for element in range(len(input_sequence)):
        if input_sequence[element] <= deleted_num:
            input_sequence[element] += deleted_num
        else:
            input_sequence[element] -= deleted_num
    removed_elements += deleted_num
    return removed_elements


sequence = list(map(int, input().split()))
sum_of_removed_elements = 0
while sequence:
    index = int(input())
    if is_invalid_index(index, sequence):
        sum_of_removed_elements += handle_invalid_index(index, sequence,)
    else:
        sum_of_removed_elements += handle_valid_index(index, sequence,)

print(sum_of_removed_elements)
