budget = float(input())
season = input()
destination = ''
stay_in = ''
price = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        price = budget * 0.3
        stay_in = 'Camp'
    elif season == 'winter':
        price = budget * 0.7
        stay_in = 'Hotel'
if 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        price = budget * 0.4
        stay_in = 'Camp'
    elif season == 'winter':
        price = budget * 0.8
        stay_in = 'Hotel'
if budget > 1000:
    destination = 'Europe'
    price = budget * 0.9
    stay_in = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{stay_in} - {price:.2f}')