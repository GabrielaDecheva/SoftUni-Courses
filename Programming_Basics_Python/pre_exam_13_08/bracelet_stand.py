money_per_day = float(input())
income_per_day = float(input())
total_expenses = float(input())
gift_price = float(input())

saved_money = money_per_day * 5
won_money = income_per_day * 5
total_money = saved_money + won_money
total_after_expenses = total_money - total_expenses

if total_after_expenses >= gift_price:
    print(f'Profit: {total_after_expenses:.2f} BGN, the gift has been purchased.')
else:
    diff = abs(total_after_expenses - gift_price)
    print(f'Insufficient money: {diff:.2f} BGN.')