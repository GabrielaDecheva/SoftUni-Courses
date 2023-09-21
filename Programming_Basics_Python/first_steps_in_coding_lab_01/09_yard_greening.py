sq_meters_for_greening = float(input())

price_without_discount = sq_meters_for_greening * 7.61
discount = price_without_discount * 0.18
total_price = price_without_discount - discount
print(f'The final price is {total_price} lv.')
print(f'The discount is {discount} lv.')