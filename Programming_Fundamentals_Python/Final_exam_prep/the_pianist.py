def add(musical_collection, commands):
    name_of_piece = commands[1]
    composer = commands[2]
    key = commands[3]
    if name_of_piece not in musical_collection.keys():
        musical_collection[name_of_piece] = []
        musical_collection[name_of_piece].append(composer)
        musical_collection[name_of_piece].append(key)
        print(f'{name_of_piece} by {composer} in {key} added to the collection!')
    else:
        print(f"{commands[1]} is already in the collection!")


def remove(musical_collection, commands):
    name_of_piece = commands[1]
    if name_of_piece in musical_collection.keys():
        del musical_collection[name_of_piece]
        print(f"Successfully removed {name_of_piece}!")
    else:
        print(f"Invalid operation! {name_of_piece} does not exist in the collection.")


def change_key(musical_collection, commands):
    name_of_piece = commands[1]
    new_key = commands[2]
    if name_of_piece in musical_collection.keys():
        musical_collection[name_of_piece][1] = new_key
        print(f'Changed the key of {name_of_piece} to {new_key}!')
    else:
        print(f"Invalid operation! {name_of_piece} does not exist in the collection.")


number_of_pieces = int(input())
collection = {}
for piece in range(number_of_pieces):
    current_piece = input()
    name, composer, key = current_piece.split('|')
    collection[name] = []
    collection[name].append(composer)
    collection[name].append(key)

while True:
    command = input()
    if command == 'Stop':
        break
    current_command = command.split('|')
    instruction = current_command[0]
    if instruction == 'Add':
        add(collection, current_command)
    elif instruction == 'Remove':
        remove(collection, current_command)
    elif instruction == 'ChangeKey':
        change_key(collection, current_command)

for key, item in collection.items():
    print(f"{key} -> Composer: {item[0]}, Key: {item[1]}")



