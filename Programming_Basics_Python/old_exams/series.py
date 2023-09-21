budget = float(input())
count_series = int(input())
total_price_series = 0

for _ in range(count_series):
    name_of_series = input()
    price = float(input())
    if name_of_series == 'Thrones':
        price = price * 0.5
        total_price_series += price
    elif name_of_series == 'Lucifer':
        price = price * 0.6
        total_price_series += price
    elif name_of_series == 'Protector':
        price = price * 0.7
        total_price_series += price
    elif name_of_series == 'TotalDrama':
        price = price * 0.8
        total_price_series += price
    elif name_of_series == 'Area':
        price = price * 0.9
        total_price_series += price
    else:
        total_price_series += price

diff = abs(budget - total_price_series)
if budget >= total_price_series:
    print(f'You bought all the series and left with {diff:.2f} lv.')
else:
    print(f'You need {diff:.2f} lv. more to buy the series!')