def take_odd(new_password):
    made_changes = ''
    for index in range(len(new_password)):
        if index % 2 != 0:
            made_changes += new_password[index]
    return made_changes


def cut(command, new_password):
    index = int(command[1])
    length = int(command[2])
    new_password = new_password[:index] + new_password[index + length:]
    return new_password


def substitute(command, new_password):
    substring = command[1]
    substitute_text = command[2]
    if substring in new_password:
        new_password = new_password.replace(substring, substitute_text)
        return new_password
    else:
        return False


string_to_manipulate = input()
updated_password = string_to_manipulate
while True:
    command = input()
    if command == 'Done':
        break
    current_command = command.split()
    instruction = current_command[0]
    if instruction == 'TakeOdd':
        updated_password = take_odd(updated_password)
        print(updated_password)
    elif instruction == 'Cut':
        updated_password = cut(current_command, updated_password)
        print(updated_password)
    elif instruction == 'Substitute':
        if substitute(current_command, updated_password):
            updated_password = substitute(current_command, updated_password)
            print(updated_password)
        else:
            print('Nothing to replace!')

print(f'Your password is: {updated_password}')
