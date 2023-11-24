def add_stop(new_string, commands):
    index = int(commands[1])
    string = commands[2]
    if index < len(new_string):
        new_string = new_string[:index] + string + new_string[index:]

    return new_string


def remove_stop(new_string, commands):
    start_index = int(commands[1])
    end_index = int(commands[2])
    if start_index < len(new_string) and end_index < len(new_string):
        new_string = new_string[:start_index] + new_string[end_index + 1:]

    return new_string


def switch(new_string, commands):
    old_string = commands[1]
    current_new_string = commands[2]

    if old_string in new_string:
        new_string = new_string.replace(old_string, current_new_string)

    return new_string


input_string = input()
changed_string = input_string
while True:
    command = input()
    if command == 'Travel':
        break
    current_command = command.split(':')
    instruction = current_command[0]
    if instruction == 'Add Stop':
        changed_string = add_stop(changed_string, current_command)
    elif instruction == 'Remove Stop':
        changed_string = remove_stop(changed_string, current_command)
    elif instruction == 'Switch':
        changed_string = switch(changed_string, current_command)
    print(changed_string)
print(f'Ready for world tour! Planned stops: {changed_string}')
