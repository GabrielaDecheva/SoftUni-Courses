increase = input()

current_increase = 0
total = 0
while increase != 'NoMoreMoney':
    amount = float(increase)
    if amount < 0:
        print('Invalid operation!')
        break
    total += amount
    print(f'Increase: {amount:.2f}')
    increase = input()

print(f'Total: {total:.2f}')