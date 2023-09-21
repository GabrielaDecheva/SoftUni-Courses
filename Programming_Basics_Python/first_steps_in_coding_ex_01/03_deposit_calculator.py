deposit_amount = float(input())
deposit_months = int(input())
percent_per_year = float(input())

total_interest = deposit_amount * percent_per_year / 100
interest_for_one_month = total_interest / 12
total_value = deposit_amount + (deposit_months * interest_for_one_month)

print(total_value)