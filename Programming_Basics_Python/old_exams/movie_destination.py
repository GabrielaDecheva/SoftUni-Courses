budget = float(input())
destination = input()
season = input()
count_days = int(input())

price_per_day = 0

if destination == 'Dubai':
    if season == 'Winter':
        price_per_day = 45000
    elif season == 'Summer':
        price_per_day = 40000
elif destination == 'Sofia':
    if season == 'Winter':
        price_per_day = 17000
    elif season == 'Summer':
        price_per_day = 12500
elif destination == 'London':
    if season == 'Winter':
        price_per_day = 24000
    elif season == 'Summer':
        price_per_day = 20250

total = price_per_day * count_days

if destination == 'Dubai':
    total = total * 0.7
if destination == 'Sofia':
    total = total + (total * 0.25)

diff = abs(budget-total)

if budget >= total:
    print(f'The budget for the movie is enough! We have {diff:.2f} leva left!')
elif budget < total:
    print(f'The director needs {diff:.2f} leva more!')
