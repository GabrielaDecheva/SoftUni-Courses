hour = int(input())
day_of_week = input()

if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Wednesday' or day_of_week == 'Thursday'\
        or day_of_week == 'Friday' or day_of_week == 'Saturday':
    if 10 <= hour <= 18:
        print('open')
    else:
        print('closed')
if day_of_week == 'Sunday':
    print('closed')
    
