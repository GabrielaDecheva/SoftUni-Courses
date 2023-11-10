string = input()
while string != 'end':
    new_string = string[::-1]
    print(f'{string} = {new_string}')
    string = input()