budget = float(input())
litres_fuel = float(input())
day = input()

price_fuel = litres_fuel * 2.1
total_with_gid = price_fuel + 100

if day == 'Saturday':
    total_with_gid = total_with_gid * 0.9
elif day == 'Sunday':
    total_with_gid = total_with_gid * 0.8

diff = abs(budget - total_with_gid)
if budget >= total_with_gid:
    print(f'Safari time! Money left: {diff:.2f} lv.')
else:
    print(f'Not enough money! Money needed: {diff:.2f} lv.')