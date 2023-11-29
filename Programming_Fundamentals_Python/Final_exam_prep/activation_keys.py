def contains(changed_key, current_command):
    substring = current_command[1]
    if substring in changed_key:
        print(f"{changed_key} contains {substring}")
    else:
        print(f"Substring not found!")


def flip(changed_key, current_command):
    case = current_command[1]
    start_index = int(current_command[2])
    end_index = int(current_command[3])
    new_part = ''
    for index in range(start_index, end_index):
        new_part += changed_key[index]
    if case == 'Upper':
        changed_key = changed_key[:start_index] + new_part.upper() + changed_key[end_index:]
    elif case == 'Lower':
        changed_key = changed_key[:start_index] + new_part.lower() + changed_key[end_index:]

    return changed_key


def slice(changed_key, current_command):
    start_index = int(current_command[1])
    end_index = int(current_command[2])
    changed_key = changed_key[:start_index] + changed_key[end_index:]

    return changed_key


raw_key = input()
updated_key = raw_key
while True:
    command = input().split('>>>')
    if command[0] == 'Generate':
        break
    instructions = command[0]
    if instructions == 'Contains':
        contains(updated_key, command)
    elif instructions == 'Flip':
        updated_key = flip(updated_key, command)
        print(updated_key)
    elif instructions == 'Slice':
        updated_key = slice(updated_key, command)
        print(updated_key)

print(f"Your activation key is: {updated_key}")

