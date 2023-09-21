city = input()
sales = float(input())
comission = 0

wrong_data = False

if city == 'Sofia':
    if 0 <= sales <= 500:
        comission = sales * 0.05
    elif 500 < sales <= 1000:
        comission = sales * 0.07
    elif 1000 < sales <= 10000:
        comission = sales * 0.08
    elif sales > 10000:
        comission = sales * 0.12
    else:
        wrong_data = True
elif city == 'Varna':
    if 0<= sales <= 500:
        comission = sales * 0.045
    elif 500 < sales <= 1000:
        comission = sales * 0.075
    elif 1000 < sales <= 10000:
        comission = sales * 0.1
    elif sales > 10000:
        comission = sales * 0.13
    else:
        wrong_data = True
elif city == 'Plovdiv':
    if 0 <= sales <= 500:
        comission = sales * 0.055
    elif 500 < sales <= 1000:
        comission = sales * 0.08
    elif 1000 < sales <= 10000:
        comission = sales * 0.12
    elif sales > 10000:
        comission = sales * 0.145
    else:
        wrong_data = True
else:
    wrong_data = True


if wrong_data:
    print('error')
else:
    print(f'{comission:.2f}')





