floors = int(input())
rooms = int(input())
room_type = ''
for floor in range(floors, 0, -1):
    for room in range(0, rooms):
        if floor == floors:
            room_type = 'L'
            print(f'{room_type}{floor}{room}', end=' ')
        elif floor % 2 and floor != floors:
            room_type = 'A'
            print(f'{room_type}{floor}{room}', end=' ')
        else:
            room_type = 'O'
            print(f'{room_type}{floor}{room}', end=' ')

    print('')
