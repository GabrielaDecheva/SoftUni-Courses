fire_cells = input().split('#')
water = int(input())
total_effort = 0
total_fire = 0
fire_cells_list = []

for current_fire_cell in fire_cells:
    split_fire_cells = current_fire_cell.split(' = ')
    type_of_fire = split_fire_cells[0]
    value_of_cell = int(split_fire_cells[1])

    if water < value_of_cell:
        continue
    if value_of_cell < 1 or value_of_cell > 125:
        continue
    if type_of_fire == 'High' and 81 <= value_of_cell <= 125:
        water -= value_of_cell
        total_effort += value_of_cell * 0.25
        total_fire += value_of_cell
        fire_cells_list.append(value_of_cell)
    elif type_of_fire == 'Medium' and 51 <= value_of_cell <= 80:
        water -= value_of_cell
        total_effort += value_of_cell * 0.25
        total_fire += value_of_cell
        fire_cells_list.append(value_of_cell)
    elif type_of_fire == 'Low' and 1 <= value_of_cell <= 50:
        water -= value_of_cell
        total_effort += value_of_cell * 0.25
        total_fire += value_of_cell
        fire_cells_list.append(value_of_cell)

print("Cells:")
for number in fire_cells_list:
    print(f" - {number}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")