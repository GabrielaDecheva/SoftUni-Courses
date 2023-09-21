age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money = 0
toys = 0
brother = 0

for year in range(1, age+1):
    if year % 2 == 0:
        money += int(year / 2) * 10
        brother += 1
    else:
        toys += 1


total_saved = (money - brother) + (toys * toy_price)

diff = abs(total_saved - washing_machine_price)

if total_saved >= washing_machine_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')