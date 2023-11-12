string_num_pairs = input()
current_pair = ''
count_repetitions = ''
final_print = ''
for index in range(len(string_num_pairs)):
    if not string_num_pairs[index].isdigit():
        current_pair += string_num_pairs[index].upper()
    else:
        for digit in range(index, len(string_num_pairs)):
            if not string_num_pairs[digit].isdigit():
                break
            count_repetitions += string_num_pairs[digit]
        final_print += current_pair * int(count_repetitions)
        current_pair = ''
        count_repetitions = ''

print(f'Unique symbols used: {len(set(final_print))}')
print(final_print)