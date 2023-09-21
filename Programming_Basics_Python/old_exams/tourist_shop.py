budget = float(input())
flag = False
total_price = 0
expenses = budget
count_products = 0
input_line = input()

while input_line != 'Stop':
    product = input_line
    product_price = float(input())
    count_products += 1
    if count_products % 3 == 0:
        product_price = product_price / 2
    total_price += product_price
    if expenses < product_price:
        flag = True
        break
    expenses -= product_price
    input_line = input()

if flag:
    diff = abs(budget - total_price)
    print(f"You don't have enough money!")
    print(f'You need {diff:.2f} leva!')
else:
    print(f'You bought {count_products} products for {total_price:.2f} leva.')