width = int(input())
length = int(input())
height = int(input())

space_apartment = width * length * height
no_more_space = False
total_boxes = 0

input_line = input()
while input_line != 'Done':
    current_boxes = int(input_line)
    total_boxes += current_boxes

    if total_boxes >= space_apartment:
        no_more_space = True
        break

    input_line = input()

diff = abs(space_apartment - total_boxes)
if no_more_space:
    print(f'No more free space! You need {diff} Cubic meters more.')
else:
    print(f'{diff} Cubic meters left.')