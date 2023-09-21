count_days = int(input())
count_hours_per_day = int(input())
current_amount = 0
total_amount = 0
for day in range(1, count_days + 1):
    for hour in range(1, count_hours_per_day + 1):
        if day % 2 == 0 and hour % 2:
            current_amount += 2.5
        elif day % 2 and hour % 2 == 0:
            current_amount += 1.25
        elif day % 2 and hour % 2 :
            current_amount += 1
        elif day %2 == 0 and hour % 2 == 0:
            current_amount += 1
    print(f'Day: {day} - {current_amount:.2f} leva')
    total_amount += current_amount
    current_amount = 0

print(f'Total: {total_amount:.2f} leva')