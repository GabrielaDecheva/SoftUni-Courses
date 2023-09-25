n = int(input())
tank_capacity = 255
added_water = 0

for _ in range(n):
    current_litres = int(input())
    if current_litres > tank_capacity - added_water:
        print(f'Insufficient capacity!')
        continue
    added_water += current_litres
print(added_water)