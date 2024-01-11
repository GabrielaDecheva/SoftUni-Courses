from collections import deque

current_water = int(input())

people = deque()
name = input()

while name != 'Start':
    people.append(name)
    name = input()

command = input()
while command != 'End':
    data = command.split()
    if len(data) == 1:
        liters_req = int(data[0])
        person = people.popleft()

        if current_water >= liters_req:
            print(f'{person} got water')
            current_water -= liters_req
        else:
            print(f'{person} must wait')
    elif len(data) == 2:
        _, liters_add = data
        # liters_add = data[1]
        current_water += int(liters_add)

    command = input()

print(f'{current_water} liters left')