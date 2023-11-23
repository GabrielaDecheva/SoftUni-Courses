def change(input_string, instructions):
    substring = instructions[1]
    replacement = instructions[2]
    new_string = input_string.replace(substring, replacement)
    return new_string


def insert(input_string, instructions):
    index = int(instructions[1])
    value = instructions[2]
    new_string = input_string[:index] + value + input_string[index:]
    return new_string


def move(input_string, instructions):
    num_letters = int(instructions[1])
    new_string = input_string[num_letters:] + input_string[:num_letters]
    return new_string


message = input()
new_message = message
while True:
    command = input()
    if command == 'Decode':
        break
    instructions = command.split('|')
    if instructions[0] == 'ChangeAll':
        new_message = change(new_message, instructions)
    elif instructions[0] == 'Insert':
        new_message = insert(new_message, instructions)
    elif instructions[0] == 'Move':
        new_message = move(new_message, instructions)
print(f'The decrypted message is: {new_message}')