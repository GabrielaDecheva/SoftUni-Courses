profit_needed = float(input())

flag = False
current_income = 0
total_income = 0

init_input = input()
while init_input != 'Party!':
    cocktail_count = int(input())
    current_income = len(init_input) * cocktail_count
    if current_income % 2 != 0:
        current_income = current_income * 0.75

    total_income += current_income

    if profit_needed <= total_income:
        flag = True
        break

    init_input = input()


if flag:
    print('Target acquired.')
    print(f'Club income - {total_income:.2f} leva.')
else:
    diff = profit_needed - total_income
    print(f'We need {diff:.2f} leva more.')
    print(f'Club income - {total_income:.2f} leva.')


