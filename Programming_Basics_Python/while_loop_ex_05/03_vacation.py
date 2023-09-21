needed_amount = float(input())
balance = float(input())
total_days = 0
spend_days = 0
flag = False
total_balance = balance
while total_balance < needed_amount:
    action = input()
    amount = float(input())
    total_days += 1
    if action == 'spend':
        total_balance -= amount
        if total_balance < 0:
            total_balance = 0
        spend_days += 1
        if spend_days == 5:
            flag = True
            break
    else:
        total_balance += amount
        spend_days = 0

if flag:
    print(f"You can't save the money.")
    print(total_days)
else:
    print(f'You saved the money for {total_days} days.')
