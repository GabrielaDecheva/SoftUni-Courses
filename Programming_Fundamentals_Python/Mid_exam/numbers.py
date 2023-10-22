input_numbers = list(map(int, input().split()))

while True:
    input_command = input().split()
    command = input_command[0]
    if command == 'Finish':
        print(*input_numbers)
        break
    elif command == 'Add':
        value = int(input_command[1])
        input_numbers.append(value)
    elif command == 'Remove':
        value = int(input_command[1])
        if value in input_numbers:
            input_numbers.remove(value)
    elif command == 'Replace':
        value1 = int(input_command[1])
        value2 = int(input_command[2])
        if value1 in input_numbers and value2 in input_numbers:
            first_index = input_numbers.index(value1)
            second_index = input_numbers.index(value2)
            input_numbers[first_index], input_numbers[second_index] = input_numbers[second_index], input_numbers[first_index]
    elif command == 'Collapse':
        value = int(input_command[1])
        input_numbers = [num for num in input_numbers if num >= value]