count_excursions_sea = int(input())
count_excursions_mountain = int(input())

profit = 0
sea_counter = count_excursions_sea
mountain_counter = count_excursions_mountain
flag = False

input_line = input()

while input_line != 'Stop':
    type_excursion = input_line
    if type_excursion == 'sea' and sea_counter > 0:
        profit += 680
        sea_counter -= 1
    elif type_excursion == 'mountain' and mountain_counter > 0:
        profit += 499
        mountain_counter -= 1
    if sea_counter == 0 and mountain_counter == 0:
        flag = True
        break
    input_line = input()

if flag:
    print(f'Good job! Everything is sold.')
    print(f'Profit: {profit} leva.')
else:
    print(f'Profit: {profit} leva.')