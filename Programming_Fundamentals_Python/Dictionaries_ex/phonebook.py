phonebook = {}
while True:
    command = input()
    if '-' not in command:
        break
    name, phone = command.split('-')
    phonebook[name] = phone

people_to_search = int(command)
for people in range(people_to_search):
    name_to_search = input()
    if name_to_search in phonebook.keys():
        print(f'{name_to_search} -> {phonebook[name_to_search]}')
    else:
        print(f'Contact {name_to_search} does not exist.')
