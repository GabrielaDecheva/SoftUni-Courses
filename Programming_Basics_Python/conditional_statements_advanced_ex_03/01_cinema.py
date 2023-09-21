type_ticket = input()
rows = int(input())
columns = int(input())

income = 0
capacity = rows * columns

if type_ticket == 'Premiere':
    income = capacity * 12
elif type_ticket == 'Normal':
    income = capacity * 7.5
elif type_ticket == 'Discount':
    income = capacity * 5
print(f'{income:.2f} leva')