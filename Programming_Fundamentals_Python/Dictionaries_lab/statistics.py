products = {}

while True:
    info = input()

    if info == 'statistics':
        print('Products in stock:')
        break
    else:
        product, quantity = info.split(': ')
        quantity = int(quantity)
        if product in products:
            products[product] += quantity
        else:
            products[product] = quantity


total_products = len(products)
total_quantity = sum(products.values())

for product, quantity in products.items():
    print(f'- {product}: {quantity}')

print(f'Total Products: {total_products}')
print(f'Total Quantity: {total_quantity}')

