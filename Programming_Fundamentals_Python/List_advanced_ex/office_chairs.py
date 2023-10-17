def check_rooms(number_of_rooms):
    free_chairs_left = 0
    for number_of_room in range(1, number_of_rooms + 1):
        chairs_in_current_room, visitors = input().split()
        diff = len(chairs_in_current_room) - int(visitors)
        if diff < 0:
            print(f'{abs(diff)} more chairs needed in room {number_of_room}')
        free_chairs_left += diff
    return free_chairs_left


rooms_count = int(input())
total_free_chairs = check_rooms(rooms_count)
if total_free_chairs >= 0:
    print(f'Game On, {total_free_chairs} free chairs left')