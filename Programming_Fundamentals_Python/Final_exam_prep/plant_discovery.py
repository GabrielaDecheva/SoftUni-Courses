def rate(command, plants_dict):
    name_of_the_plant = command[1].rstrip()
    rating_of_the_plant = int(command[2])
    if name_of_the_plant not in plants_dict.keys():
        print('error')
    else:
        plants_dict[name_of_the_plant]['ratings'].append(rating_of_the_plant)
    return plants_dict


def update(command, plants_dict):
    name_of_the_plant = command[1].rstrip()
    new_rarity = int(command[2])
    if name_of_the_plant not in plants_dict.keys():
        print('error')
    else:
        plants_dict[name_of_the_plant]['rarity'] = new_rarity
    return plants_dict


def reset(command, plants_dict):
    name_of_the_plant = command[1].rstrip()
    if name_of_the_plant not in plants_dict.keys():
        print('error')
    else:
        plants_dict[name_of_the_plant]['ratings'].clear()
    return plants_dict


count_lines = int(input())
plants = {}
for _ in range(count_lines):
    plant_info = input().split('<->')
    name_of_plant = plant_info[0]
    rarity = int(plant_info[1])
    plants[name_of_plant] = {'rarity': rarity, 'ratings': []}

while True:
    commands = input()
    if commands == 'Exhibition':
        break
    updated_command = commands.replace('-', ':')
    command_info = updated_command.split(': ')
    current_command = command_info[0]
    if current_command == 'Rate':
        rate(command_info, plants)
    elif current_command == 'Update':
        update(command_info, plants)
    elif current_command == 'Reset':
        reset(command_info, plants)

print('Plants for the exhibition:')
for plant, plant_info in plants.items():
    if len(plant_info['ratings']) > 0:
        all_ratings = sum(plant_info['ratings'])
        average_rating = all_ratings / len(plant_info['ratings'])
    else:
        average_rating = 0
    print(f'- {plant}; Rarity: {plant_info["rarity"]}; Rating: {average_rating:.2f}')