def fishing(position, fishing_area, fish_amount):
    fish_amount += int(fishing_area[position[0]][position[1]])
    fishing_area[position[0]][position[1]] = "-"

    return fish_amount, fishing_area


def ship_sank(position, is_sank=False):
    r, c = position[0], position[1]

    return (f"You fell into a whirlpool! The ship sank and you lost the fish you caught."
            f" Last coordinates of the ship: [{r},{c}]")


def move_sailor(command, position, fishing_area):
    row, col = position
    fishing_area[row][col] = '-'

    if command == "up":
        position[0] -= 1
    elif command == "down":
        position[0] += 1
    elif command == "left":
        position[1] -= 1
    elif command == "right":
        position[1] += 1

    return position


def handle_boundaries(position, size_of_are):
    for i in range(2):
        if position[i] < 0:
            position[i] = size_of_are - 1
        elif position[i] >= size_of_are:
            position[i] = 0


def fill_fishing_area(size_of_area):
    fishing_area = []
    for _ in range(size_of_area):
        fishing_area.append(list(input()))
    return fishing_area


def find_start_position(size_of_area, fishing_area):
    for i in range(size_of_area):
        for j in range(size_of_area):
            if fishing_area[i][j] == 'S':
                return [i, j]
    return None


size = int(input())
fishing_area_matrix = fill_fishing_area(size)
current_position = find_start_position(size, fishing_area_matrix)
min_fish_tons = 20
fish_caught = 0

command_line = input()
while command_line != "collect the nets":
    current_position = move_sailor(command_line, current_position, fishing_area_matrix)
    handle_boundaries(current_position, size)

    if fishing_area_matrix[current_position[0]][current_position[1]] == "W":
        sank = True
        print(ship_sank(current_position, sank))
        exit()
    elif fishing_area_matrix[current_position[0]][current_position[1]].isdigit():
        fish_caught, fishing_area_matrix = fishing(current_position, fishing_area_matrix, fish_caught)

    fishing_area_matrix[current_position[0]][current_position[1]] = 'S'
    command_line = input()

if fish_caught >= min_fish_tons:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! "
          f"You need {min_fish_tons - fish_caught} tons of fish more.")
if fish_caught > 0:
    print(f"Amount of fish caught: {fish_caught} tons.")

for row in fishing_area_matrix:
    print("".join(row))