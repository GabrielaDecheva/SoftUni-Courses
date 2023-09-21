capacity_hall = int(input())
ticket_price = 5
count_people = 0
total_income = 0
current_income = 0
flag = False
input_line = input()

while input_line != 'Movie time!':
    current_people = int(input_line)
    if current_people > (capacity_hall - count_people):
        flag = True
        break
    count_people += current_people
    if current_people % 3 == 0:
        current_income = (current_people * ticket_price) - 5
        total_income += current_income
    else:
        current_income = current_people * ticket_price
        total_income += current_income

    input_line = input()

if flag:
    print('The cinema is full.')
    print(f'Cinema income - {total_income} lv.')
else:
    diff = capacity_hall - count_people
    print(f'There are {diff} seats left in the cinema.')
    print(f'Cinema income - {total_income} lv.')


