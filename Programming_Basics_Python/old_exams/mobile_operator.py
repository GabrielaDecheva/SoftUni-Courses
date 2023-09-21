contract_years = input()
type_contract = input()
mobile_network = input()
months_to_pay = int(input())

price_per_month = 0

if contract_years == 'one':
    if type_contract == 'Small':
        price_per_month = 9.98
    elif type_contract == 'Middle':
        price_per_month = 18.99
    elif type_contract == 'Large':
        price_per_month = 25.98
    elif type_contract == 'ExtraLarge':
        price_per_month = 35.99
elif contract_years == 'two':
    if type_contract == 'Small':
        price_per_month = 8.58
    elif type_contract == 'Middle':
        price_per_month = 17.09
    elif type_contract == 'Large':
        price_per_month = 23.59
    elif type_contract == 'ExtraLarge':
        price_per_month = 31.79

if mobile_network == 'yes':
    if price_per_month <= 10:
        price_per_month += 5.50
    elif price_per_month <= 30:
        price_per_month += 4.35
    elif price_per_month > 30:
        price_per_month += 3.85

total = price_per_month * months_to_pay
if contract_years == 'two':
    total = total * 0.9625

print(f'{total:.2f} lv.')