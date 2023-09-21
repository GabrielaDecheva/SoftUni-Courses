days = int(input())
type_room = input()
rate = input()

total_price = 0

if type_room == 'room for one person':
    if days < 10:
        total_price = (days - 1) * 18
    elif 10 <= days <= 15:
        total_price = (days - 1) * 18
    elif days > 15:
        total_price = (days - 1) * 18
elif type_room == 'apartment':
    if days < 10:
        total_price = ((days - 1) * 25) * 0.7
    elif 10 <= days <= 15:
        total_price = ((days - 1) * 25) * 0.65
    elif days > 15:
        total_price = ((days - 1) * 25) * 0.5
elif type_room == 'president apartment':
    if days < 10:
        total_price = ((days - 1) * 35) * 0.9
    elif 10 <= days <= 15:
        total_price = ((days - 1) * 35) * 0.85
    elif days > 15:
        total_price = ((days - 1) * 35) * 0.8

if rate == 'positive':
    total_price = total_price + (total_price * 0.25)
elif rate == 'negative':
    total_price = total_price * 0.9

print(f'{total_price:.2f}')