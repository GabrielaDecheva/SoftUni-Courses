budget = float(input())
videocard_count = int(input())
processor_count = int(input())
ram_count = int(input())

videocard_amount = videocard_count * 250
processor_amount = processor_count * (videocard_amount * 0.35)
ram_amount = ram_count * (videocard_amount * 0.10)

total_price = videocard_amount + processor_amount + ram_amount

if videocard_count > processor_count:
    total_price = total_price - (total_price * 0.15)

diff = abs(budget - total_price)

if budget >= total_price:
    print(f'You have {diff:.2f} leva left!')
else:
    print(f'Not enough money! You need {diff:.2f} leva more!')