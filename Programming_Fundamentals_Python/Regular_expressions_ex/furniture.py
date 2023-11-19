import re

input_line = input()
pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
bought_furniture = []
total_cost = 0
while input_line != 'Purchase':
    match = re.search(pattern, input_line)
    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        total_cost += float(price) * int(quantity)
    input_line = input()
print('Bought furniture:')
for furniture in bought_furniture:
    print(furniture)
print(f'Total money spend: {total_cost:.2f}')