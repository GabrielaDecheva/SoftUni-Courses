n = int(input())
total = 0
for i in range(n):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100.00:
        continue
    if days < 1 or days > 31:
        continue
    if capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    total_order = (price_per_capsule * capsules_per_day) * days
    print(f'The price for the coffee is: ${total_order:.2f}')
    total += total_order

print(f'Total: ${total:.2f}')