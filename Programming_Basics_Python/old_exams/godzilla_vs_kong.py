budget = float(input())
count_statists = int(input())
price_clothes_per_statist = float(input())

decor = budget * 0.1
price_all_clothes = count_statists * price_clothes_per_statist

if count_statists > 150:
    price_all_clothes = price_all_clothes * 0.9

total = decor + price_all_clothes

diff = abs(budget - total)

if budget >= total:
    print(f'Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')
else:
    print(f'Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')
