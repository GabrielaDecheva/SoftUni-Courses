first_number = int(input())
second_number = int(input())
operator = input()

result = 0
zero_flag = False

if operator == '+':
    result = first_number + second_number
elif operator == '-':
    result = first_number - second_number
elif operator == '*':
    result = first_number * second_number
elif operator == '/':
    if second_number == 0:
        zero_flag = True
    else:
        result = first_number / second_number
elif operator == '%':
    if second_number == 0:
        zero_flag = True
    else:
        result = first_number % second_number

if operator == '+' or operator == '-' or operator == '*':
    if result % 2 == 0:
        print(f'{first_number} {operator} {second_number} = {result} - even')
    else:
        print(f'{first_number} {operator} {second_number} = {result} - odd')
elif operator == '/':
    if zero_flag:
        print(f'Cannot divide {first_number} by zero')
    else:
        print(f'{first_number} {operator} {second_number} = {result:.2f}')
elif operator == '%':
    if zero_flag:
        print(f'Cannot divide {first_number} by zero')
    else:
        print(f'{first_number} {operator} {second_number} = {result}')