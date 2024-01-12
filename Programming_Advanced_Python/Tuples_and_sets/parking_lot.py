n = int(input())

cars = set()

for _ in range(n):
    direction, car_num = input().split(', ')
    if direction == "IN":
        cars.add(car_num)
    elif direction == "OUT":
        if car_num in cars:
            cars.remove(car_num)

if cars:
    for car in cars:
        print(car)
else:
    print('Parking Lot is Empty')
