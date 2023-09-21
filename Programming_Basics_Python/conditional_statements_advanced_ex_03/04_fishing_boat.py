budget = int(input())
season = input()
count_people = int(input())

rent = 0

if season == 'Spring':
    rent = 3000
elif season == 'Summer' or season == 'Autumn':
    rent = 4200
elif season == 'Winter':
    rent = 2600

if count_people <= 6:
        rent = rent * 0.9
elif 7 <= count_people <= 11:
        rent = rent * 0.85
elif count_people >= 12:
        rent = rent * 0.75

if count_people % 2 == 0 and season != 'Autumn':
        rent = rent * 0.95

diff = abs(budget - rent)

if budget >= rent:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')
