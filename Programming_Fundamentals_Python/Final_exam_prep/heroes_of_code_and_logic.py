def cast_spell(heroes_dictionary, current_command):
    name_of_hero = current_command[1]
    mana_needed = int(current_command[2])
    spell_name = current_command[3]
    if heroes_dictionary[name_of_hero]['mp'] >= mana_needed:
        heroes_dictionary[name_of_hero]['mp'] -= mana_needed
        print(f"{name_of_hero} has successfully cast {spell_name} and now has "
              f"{heroes_dictionary[name_of_hero]['mp']} MP!")
    else:
        print(f"{name_of_hero} does not have enough MP to cast {spell_name}!")
    return heroes_dictionary


def take_damage(heroes_dictionary, current_command):
    name_of_hero = current_command[1]
    damage = int(current_command[2])
    attacker = current_command[3]
    heroes_dictionary[name_of_hero]['hp'] -= damage
    if heroes_dictionary[name_of_hero]['hp'] > 0:
        print(f"{name_of_hero} was hit for {damage} HP by {attacker} and now has {heroes_dictionary[name_of_hero]['hp']} HP left!")
    else:
        del heroes_dictionary[name_of_hero]
        print(f"{name_of_hero} has been killed by {attacker}!")
    return heroes_dictionary


def recharge(heroes_dictionary, current_command):
    name_of_hero = current_command[1]
    amount = int(current_command[2])
    amount_recovered = min(amount, (200 - heroes_dictionary[name_of_hero]['mp']))
    heroes_dictionary[name_of_hero]['mp'] += amount_recovered

    print(f"{name_of_hero} recharged for {amount_recovered} MP!")
    return heroes_dictionary


def heal(heroes_dictionary, current_command):
    name_of_hero = current_command[1]
    amount = int(current_command[2])
    amount_recovered = min(amount, (100 - heroes_dictionary[name_of_hero]['hp']))
    heroes_dictionary[name_of_hero]['hp'] += amount_recovered

    print(f"{name_of_hero} healed for {amount_recovered} HP!")
    return heroes_dictionary


number_of_heroes = int(input())
heroes_info_dict = {}
for hero in range(number_of_heroes):
    hero_information = input().split()
    hero_name = hero_information[0]
    hit_points = int(hero_information[1])
    mana_points = int(hero_information[2])
    heroes_info_dict[hero_name] = {'hp': hit_points, 'mp': mana_points}

while True:
    command = input().split(' - ')
    if command[0] == 'End':
        break
    current_action = command[0]
    if current_action == 'CastSpell':
        heroes_info_dict = cast_spell(heroes_info_dict, command)
    elif current_action == 'TakeDamage':
        heroes_info_dict = take_damage(heroes_info_dict, command)
    elif current_action == 'Recharge':
        heroes_info_dict = recharge(heroes_info_dict, command)
    elif current_action == 'Heal':
        heroes_info_dict = heal(heroes_info_dict, command)

for hero, hero_info in heroes_info_dict.items():
    print(f"{hero}\n  HP: {hero_info['hp']}\n  MP: {hero_info['mp']}")