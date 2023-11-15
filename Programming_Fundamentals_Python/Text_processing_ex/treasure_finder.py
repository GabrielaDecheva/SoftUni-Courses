def encrypted_message(command, keys):
    decrypted_message = ''
    for key in keys:
        for char in command:
            new_char = chr(ord(char) - int(key))
            decrypted_message += new_char
            break
        continue
    return decrypted_message


keys = input().split()
while True:
    command_line = input()
    if command_line == 'find':
        break
    result = (encrypted_message(command_line, keys))
    print(result)