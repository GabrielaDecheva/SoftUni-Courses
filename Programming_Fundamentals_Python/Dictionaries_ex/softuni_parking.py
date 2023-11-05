parking_information = {}
number_of_commands = int(input())
for _ in range(number_of_commands):
    command = input().split()
    status = command[0]
    if status == 'register':
        name = command[1]
        plate_number = command[2]
        if name not in parking_information.keys():
            parking_information[name] = plate_number
            print(f"{name} registered {plate_number} successfully")
        else:
            print(f'ERROR: already registered with plate number {parking_information[name]}')
    elif status == 'unregister':
        name = command[1]
        if name not in parking_information:
            print(f"ERROR: user {name} not found")
        else:
            del parking_information[name]
            print(f"{name} unregistered successfully")
for name, licence_plate in parking_information.items():
    print(f'{name} => {licence_plate}')

