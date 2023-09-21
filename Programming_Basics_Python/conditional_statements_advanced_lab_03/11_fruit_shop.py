fruit = input()
day_of_week = input()
quantity = float(input())
price = 0
wrong_data = False

if fruit == 'banana':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday'\
            or day_of_week == 'Friday':
        price = 2.5
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        price = 2.7
    else:
        wrong_data = True
elif fruit == 'apple':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday'\
            or day_of_week == 'Friday':
        price = 1.2
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        price = 1.25
    else:
        wrong_data = True
elif fruit == 'orange':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday'\
            or day_of_week == 'Friday':
        price = 0.85
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        price = 0.9
    else:
        wrong_data = True
elif fruit == 'grapefruit':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday'\
            or day_of_week == 'Friday':
        price = 1.45
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        price = 1.6
    else:
        wrong_data = True
elif fruit == 'kiwi':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday'\
            or day_of_week == 'Friday':
        price = 2.7
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        price = 3
    else:
        wrong_data = True
elif fruit == 'pineapple':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday'\
            or day_of_week == 'Friday':
        price = 5.5
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        price = 5.6
    else:
        wrong_data = True
elif fruit == 'grapes':
    if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday'\
            or day_of_week == 'Friday':
        price = 3.85
    elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
        price = 4.2
    else:
        wrong_data = True
else:
    wrong_data = True

total = quantity * price

if wrong_data:
    print('error')
else:
    print(f'{total:.2f}')
