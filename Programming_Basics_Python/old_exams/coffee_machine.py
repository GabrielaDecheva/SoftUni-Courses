drink = input()
sugar = input()
count_drinks = int(input())

price_drink = 0

if drink == 'Espresso':
    if sugar == 'Without':
        price_drink = 0.90
    elif sugar == 'Normal':
        price_drink = 1
    elif sugar == 'Extra':
        price_drink = 1.20
elif drink == 'Cappuccino':
    if sugar == 'Without':
        price_drink = 1
    elif sugar == 'Normal':
        price_drink = 1.20
    elif sugar == 'Extra':
        price_drink = 1.60
elif drink == 'Tea':
    if sugar == 'Without':
        price_drink = 0.5
    elif sugar == 'Normal':
        price_drink = 0.6
    elif sugar == 'Extra':
        price_drink = 0.7

total_cost = count_drinks * price_drink

if sugar == 'Without':
    total_cost = total_cost * 0.65

if drink == 'Espresso' and count_drinks >= 5:
    total_cost = total_cost * 0.75

if total_cost > 15:
    total_cost = total_cost * 0.80

print(f'You bought {count_drinks} cups of {drink} for {total_cost:.2f} lv.')


