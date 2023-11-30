def plunder(cities_dict, command):
    town = command[1]
    people = int(command[2])
    gold = int(command[3])
    cities_dict[town]['population'] -= people
    cities_dict[town]['gold'] -= gold
    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
    if cities_dict[town]['population'] == 0 or cities_dict[town]['gold'] == 0:
        cities_dict.pop(town)
        print(f"{town} has been wiped off the map!")


def prosper(cities_dict, command):
    town = command[1]
    gold = int(command[2])
    if gold < 0:
        print(f"Gold added cannot be a negative number!")
    else:
        cities_dict[town]['gold'] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {cities_dict[town]['gold']} gold.")


cities_input = input().split('||')
cities_information = {}
while cities_input[0] != 'Sail':
    name = cities_input[0]
    population = int(cities_input[1])
    gold = int(cities_input[2])
    if name not in cities_information.keys():
        cities_information[name] = {'population': 0, 'gold': 0}
    cities_information[name]['population'] += population
    cities_information[name]['gold'] += gold
    cities_input = input().split('||')

command_input = input().split('=>')
while command_input[0] != 'End':
    event = command_input[0]
    if event == 'Plunder':
        plunder(cities_information, command_input)
    elif event == 'Prosper':
        prosper(cities_information, command_input)

    command_input = input().split('=>')

if cities_information:
    print(f"Ahoy, Captain! There are {len(cities_information)} wealthy settlements to go to:")
    for city, info in cities_information.items():
        print(f'{city} -> Population: {info["population"]} citizens, Gold: {info["gold"]} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")