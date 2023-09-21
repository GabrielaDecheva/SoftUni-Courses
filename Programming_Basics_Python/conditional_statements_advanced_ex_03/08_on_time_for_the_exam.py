hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arr = int(input())
minutes_of_arr = int(input())

time_in_min_exam = (hour_of_exam * 60) + minutes_of_exam
time_in_min_arr = (hour_of_arr * 60) + minutes_of_arr
diff_min = abs(time_in_min_arr - time_in_min_exam)

if time_in_min_arr > time_in_min_exam:
    print('Late')
    if diff_min >= 60:
        hour = diff_min // 60
        minutes = diff_min % 60
        print(f'{hour}:{minutes:02d} hours after the start')
    else:
        print(f"{diff_min} minutes after the start")
elif time_in_min_arr == time_in_min_exam or diff_min <= 30:
    print('On time')
    if diff_min > 0:
        print(f'{diff_min} minutes before the start')
else:
    print('Early')
    if diff_min >= 60:
        hour = diff_min // 60
        minutes = diff_min % 60
        print(f'{hour}:{minutes:02d} hours before the start')
    else:
        print(f'{diff_min} minutes before the start')

