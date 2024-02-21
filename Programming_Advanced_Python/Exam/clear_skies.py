size = int(input())
airspace = []
initial_armour_value = 300
enemies_count = 0
current_jet_position = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    airspace.append(list(input()))
    if "J" in airspace[row]:
        current_jet_position = [row, airspace[row].index("J")]
        airspace[row][current_jet_position[1]] = "-"
    enemies_count += airspace[row].count("E")

while initial_armour_value > 0 or enemies_count > 0:
    direction = input()
    new_row = current_jet_position[0] + directions[direction][0]
    new_col = current_jet_position[1] + directions[direction][1]

    current_jet_position = [new_row, new_col]
    symbol = airspace[new_row][new_col]

    if symbol == "-":
        continue
    elif symbol == "E":
        enemies_count -= 1
        airspace[new_row][new_col] = "-"
        if enemies_count == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            break
        else:
            initial_armour_value -= 100
            if initial_armour_value <= 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates "
                      f"[{current_jet_position[0]}, {current_jet_position[1]}]!")
                break
    elif symbol == "R":
        initial_armour_value = 300
        airspace[new_row][new_col] = "-"

airspace[current_jet_position[0]][current_jet_position[1]] = "J"

for row in airspace:
    print(*row, sep="")
