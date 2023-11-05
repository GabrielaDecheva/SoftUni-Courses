products = {}
command = input()
while command != 'buy':
    product_info = command.split()
    product = product_info[0]
    price = float(product_info[1])
    quantity = int(product_info[2])
    if product not in products.keys():
        products[product] = []
        products[product].append(price)
        products[product].append(quantity)
    else:
        products[product][0] = price
        products[product][1] += quantity
    command = input()

for product, info_list in products.items():
    total_price = info_list[0] * info_list[1]
    print(f'{product} -> {total_price:.2f}')