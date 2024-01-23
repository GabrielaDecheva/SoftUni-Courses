def move(direction, steps) -> list:
    r = my_position[0] + directions[direction][0] * steps
    c = my_position[1] + directions[direction][1] * steps

    if not (0 <= r < SIZE and 0 <= c < SIZE):
        return my_position
    if field[r][c] == "x":
        return my_position

    return [r, c]


def shoot(direction) -> list or None:
    r = my_position[0] + directions[direction][0]
    c = my_position[1] + directions[direction][1]

    while 0 <= r < SIZE and 0 <= c < SIZE:
        if field[r][c] == "x":
            field[r][c] = "."
            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]


SIZE = 5

field = []
my_position = []

all_targets = 0
hit_targets = 0
positions_of_hit_targets = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(SIZE):
    field.append(input().split())

    if "A" in field[row]:
        my_position = [row, field[row].index("A")]
        field[row][my_position[1]] = "."

    all_targets += field[row].count("x")

for _ in range(int(input())):
    command_line = input().split() # move up 4 | shoot up

    if command_line[0] == "move":
        my_position = move(command_line[1], int(command_line[2]))
    elif command_line[0] == 'shoot':
        target_pos = shoot(command_line[1])

        if target_pos:
            positions_of_hit_targets.append(target_pos)
            hit_targets += 1
        if hit_targets == all_targets:
            print(f"Training completed! All {all_targets} targets hit.")
            break

if hit_targets < all_targets:
    print(f"Training not completed! {all_targets - hit_targets} targets left.")

print(*positions_of_hit_targets, sep="\n")


