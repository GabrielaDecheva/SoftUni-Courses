def data_types(command, input_line):
    result = ''
    if command == 'int':
        result = int(input_line) * 2
    elif command == 'real':
        result = f'{float(input_line) * 1.5:.2f}'
    elif command == 'string':
        result = f'${input_line}$'
    return result


command_line = input()
second_command_line = input()
print(data_types(command_line, second_command_line))
