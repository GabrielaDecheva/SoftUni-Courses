force_dict = {}
command = input()
while command != 'Lumpawaroo':
    if '|' in command:
        force_side, force_user = command.split(' | ')
        user_exists = False
        for value in force_dict.values():
            if force_user in value:
                user_exists = True
                break
        if not user_exists:
            if force_side not in force_dict.keys():
                force_dict[force_side] = []
            force_dict[force_side].append(force_user)
    elif '->' in command:
        force_user, force_side = command.split(' -> ')
        for value in force_dict.values():
            if force_user in value:
                value.remove(force_user)
                break
        if force_side not in force_dict.keys():
            force_dict[force_side] = []
        force_dict[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()
for force_side, force_user in force_dict.items():
    if len(force_user) > 0:
        print(f"Side: {force_side}, Members: {len(force_user)}")
        for user in force_user:
            print(f'! {user}')
