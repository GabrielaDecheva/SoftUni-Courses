sequence_of_nums = list(map(int, input(). split(', ')))
group = 10

while sequence_of_nums:
    filtered_nums = [num for num in sequence_of_nums if num <= group]
    print(f"Group of {group}'s: {filtered_nums}")
    group += 10
    sequence_of_nums = [num for num in sequence_of_nums if num not in filtered_nums]

