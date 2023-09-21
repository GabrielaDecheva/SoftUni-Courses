input_line = input()
flag = False

while input_line != 'End':
    destination = input_line
    budget = float(input())
    saved_money = 0
    while saved_money < budget:
        current_amount = float(input())
        saved_money += current_amount
        if saved_money >= budget:
            flag = True
            print(f'Going to {destination}!')
            break
    input_line = input()


