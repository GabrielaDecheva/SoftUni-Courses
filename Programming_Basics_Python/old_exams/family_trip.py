budget = float(input())
count_nights = int(input())
price_per_night = float(input())
percent_add_expenses = int(input())

total_cost_nights = count_nights * price_per_night

if count_nights > 7:
    price_per_night = price_per_night * 0.95
    total_cost_nights = count_nights * price_per_night
else:
    total_cost_nights = count_nights * price_per_night

add_expenses_amount = budget * (percent_add_expenses / 100)

total = total_cost_nights + add_expenses_amount

diff = abs(budget - total)

if budget >= total:
    print(f'Ivanovi will be left with {diff:.2f} leva after vacation.')
else:
    print(f'{diff:.2f} leva needed.')