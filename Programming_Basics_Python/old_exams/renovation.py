import math

height_wall = int(input())
width_wall = int(input())
percent_no_paint = int(input())

total_walls = height_wall * width_wall * 4
total_for_painting = math.ceil(total_walls - (total_walls * (percent_no_paint / 100)))

input_line = input()
while input_line != 'Tired!':
    litres = int(input_line)
    total_for_painting -= litres
    if total_for_painting <= 0:
        break

    input_line = input()

if total_for_painting == 0:
    print('All walls are painted! Great job, Pesho!')
elif total_for_painting < 0:
    print(f'All walls are painted and you have {abs(total_for_painting)} l paint left!')
else:
    print(f'{total_for_painting} quadratic m left.')