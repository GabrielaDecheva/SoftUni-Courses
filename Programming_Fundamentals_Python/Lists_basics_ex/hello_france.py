items = input().split('|')
budget = float(input())

list_items = []

for current_item in items:
    split_items = current_item.split('->')
    type_of_item = split_items[0]
    price_of_item = float(split_items[1])

    if type_of_item == 'Clothes':
        if price_of_item <= 50.00 and price_of_item < budget:
            budget -= price_of_item
            list_items.append(price_of_item)
    elif type_of_item == 'Shoes':
        if price_of_item <= 35.00 and price_of_item < budget:
            budget -= price_of_item
            list_items.append(price_of_item)
    elif type_of_item == 'Accessories':
        if price_of_item <= 20.50 and price_of_item < budget:
            budget -= price_of_item
            list_items.append(price_of_item)

updated_price = 0
profit = 0
new_budget = budget
for prices in list_items:
    updated_price += prices + (prices * 0.4)
    print(updated_price, end=' ')
    new_budget += updated_price
    profit += updated_price - prices
    updated_price = 0
print()
print(f'Profit: {profit:.2f}')

if new_budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')