budget = int(input())

total_prices = 0

while True:
    command = input()
    if command == 'End':
        print('You bought everything needed.')
        break
    current_price = float(command)

    if current_price + total_prices > budget:
        print('You went in overdraft!')
        break
    total_prices += current_price