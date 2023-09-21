type_flower = input()
count_flower = int(input())
budget = int(input())

total_price = 0

if type_flower == 'Roses':
    total_price = count_flower * 5
    if count_flower > 80:
        total_price = total_price * 0.9
elif type_flower == 'Dahlias':
    total_price = count_flower * 3.8
    if count_flower > 90:
        total_price = total_price * 0.85
elif type_flower == 'Tulips':
    total_price = count_flower * 2.8
    if count_flower > 80:
        total_price = total_price * 0.85
elif type_flower == 'Narcissus':
    total_price = count_flower * 3
    if count_flower < 120:
        total_price = total_price * 1.15
elif type_flower == 'Gladiolus':
    total_price = count_flower * 2.5
    if count_flower < 80:
        total_price = total_price * 1.20

diff = abs(budget - total_price)

if budget >= total_price:
    print(f'Hey, you have a great garden with {count_flower} {type_flower} and {diff:.2f} leva left.')
else:
    print(f'Not enough money, you need {diff:.2f} leva more.')
