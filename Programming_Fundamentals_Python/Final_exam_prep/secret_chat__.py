def insert_space(message, current_command):
    index = int(current_command[1])
    message = message[:index] + ' ' + message[index:]
    print(message)
    return message


def reverse(message, current_command):
    substring = current_command[1]
    if substring in message:
        message = message.replace(substring, '', 1)
        reversed_substring = substring[::-1]
        message += reversed_substring
        print(message)
    else:
        print('error')
    return message


def change_all(message, current_command):
    substring = current_command[1]
    replacement = current_command[2]
    if substring in message:
        message = message.replace(substring, replacement)
    print(message)
    return message


input_message = input()
changed_message = input_message
command = input().split(':|:')
while command[0] != 'Reveal':
    instruction = command[0]
    if instruction == 'InsertSpace':
        changed_message = insert_space(changed_message, command)

    elif instruction == 'Reverse':
        changed_message = reverse(changed_message, command)

    elif instruction == 'ChangeAll':
        changed_message = change_all(changed_message, command)

    command = input().split(':|:')

print(f"You have a new text message: {changed_message}")