city = input()
package = input()
vip_discount = input()
count_days = int(input())

price_per_day = 0
wrong_data = False

if city == 'Bansko' or city == 'Borovets':
    if package == 'withEquipment':
        price_per_day = 100
        if vip_discount == 'yes':
            price_per_day = price_per_day * 0.90
    elif package == 'noEquipment':
        price_per_day = 80
        if vip_discount == 'yes':
            price_per_day = price_per_day * 0.95
    else:
        wrong_data = True

elif city == 'Varna' or city == 'Burgas':
    if package == 'withBreakfast':
        price_per_day = 130
        if vip_discount == 'yes':
            price_per_day = price_per_day * 0.88
    elif package == 'noBreakfast':
        price_per_day = 100
        if vip_discount == 'yes':
            price_per_day = price_per_day * 0.93
    else:
        wrong_data = True
else:
    wrong_data = True

if count_days > 7:
    count_days = count_days - 1

total = count_days * price_per_day

if wrong_data:
    print(f'Invalid input!')
elif count_days < 1:
    print(f'Days must be positive number!')
else:
    print(f'The price is {total:.2f}lv! Have a nice time!')