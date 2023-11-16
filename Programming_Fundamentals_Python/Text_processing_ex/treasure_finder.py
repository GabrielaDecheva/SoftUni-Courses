def encrypted_message(command, keys):
    decrypted_message = ''
    key_index = 0
    message_index = 0
    while message_index < len(command):
        decrypted_message += chr(ord(command[message_index]) - keys[key_index])
        message_index += 1
        key_index += 1
        if key_index >= len(keys):
            key_index = 0
    return decrypted_message


def type_treasure(command, keys):
    decrypted_message = encrypted_message(command, keys)
    type_of_treasure = ''
    for index in range(len(decrypted_message)):
        if decrypted_message[index] == '&':
            for i in range(index + 1, len(decrypted_message)):
                if decrypted_message[i] != '&':
                    type_of_treasure += decrypted_message[i]
                else:
                    return type_of_treasure


def coordinates(command, keys):
    decrypted_message = encrypted_message(command, keys)
    treasure_coordinates = ''
    for index in range(len(decrypted_message)):
        if decrypted_message[index] == '<':
            for i in range(index + 1, len(decrypted_message)):
                if decrypted_message[i] == '>':
                    break
                else:
                    treasure_coordinates += decrypted_message[i]
    return treasure_coordinates


keys = [int(i) for i in input().split()]
while True:
    command_line = input()
    if command_line == 'find':
        break
    result_type = type_treasure(command_line, keys)
    result_coordinates = coordinates(command_line, keys)
    print(f'Found {result_type} at {result_coordinates}')