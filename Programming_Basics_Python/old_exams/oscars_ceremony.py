hall_rent = int(input())

statue = hall_rent * 0.70
catering = statue * 0.85
sound = catering / 2

total = hall_rent + statue + catering + sound

print(f'{total:.2f}')
