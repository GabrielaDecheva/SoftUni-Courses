pen_packages = int(input())
marker_packages = int(input())
litres_detergent = int(input())
percent_discount = int(input())

total_price_pens = pen_packages * 5.8
total_price_markers = marker_packages * 7.2
total_price_detergent = litres_detergent * 1.2
total_price_without_discount = total_price_pens + total_price_markers + total_price_detergent
discount = total_price_without_discount * (percent_discount / 100)
total_amount_to_pay = total_price_without_discount - discount
print(total_amount_to_pay)