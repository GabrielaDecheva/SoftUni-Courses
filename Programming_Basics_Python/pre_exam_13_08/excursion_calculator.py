count_people = int(input())
season = input()

price = 0

if count_people <= 5:
    if season == 'spring':
        price = 50
    elif season == 'summer':
        price = 48.50
    elif season == 'autumn':
        price = 60
    elif season == 'winter':
        price = 86
elif count_people > 5:
    if season == 'spring':
        price = 48
    elif season == 'summer':
        price = 45
    elif season == 'autumn':
        price = 49.50
    elif season == 'winter':
        price = 85

total = count_people * price

if season == 'summer':
    total = total * 0.85
elif season == 'winter':
    total = total + (total * 0.08)

print(f'{total:.2f} leva.')