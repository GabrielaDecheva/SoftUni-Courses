budget = float(input())
count_statists = int(input())
price_clothes_per_statist = float(input())

decor_price = budget * 0.10
clothes = count_statists * price_clothes_per_statist

if count_statists > 150:
    clothes = clothes - (clothes * 0.10)

amount_needed = decor_price + clothes

diff = abs(budget - amount_needed)

if budget >= amount_needed:
    print('Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')