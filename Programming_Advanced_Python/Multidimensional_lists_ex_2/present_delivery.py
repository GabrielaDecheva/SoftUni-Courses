def cookies(presents_left, nice_kids):
    for coordinates in directions.values():
        row = santa_start_position[0] + coordinates[0]
        col = santa_start_position[1] + coordinates[1]

        if neighbourhood[row][col].isalpha():
            if neighbourhood[row][col] == "V":
                nice_kids += 1

            neighbourhood[row][col] = "-"
            presents_left -= 1

        if not presents_left:
            break
    return presents_left, nice_kids


count_of_presents = int(input())
size_matrix = int(input())
neighbourhood = []

total_nice_kids = 0
nice_kids_with_present = 0
santa_start_position = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size_matrix):
    neighbourhood.append(input().split())
    if "S" in neighbourhood[row]:
        santa_start_position = [row, neighbourhood[row].index("S")]
        neighbourhood[santa_start_position[0]][santa_start_position[1]] = "-"
    total_nice_kids += neighbourhood[row].count("V")

command_line = input()
while command_line != "Christmas morning":
    santa_start_position = [
        santa_start_position[0] + directions[command_line][0],
        santa_start_position[1] + directions[command_line][1]
    ]
    house_visited = neighbourhood[santa_start_position[0]][santa_start_position[1]]

    if house_visited == "V":
        if count_of_presents > 0:
            count_of_presents -= 1
            nice_kids_with_present += 1
    elif house_visited == "C":
        count_of_presents, nice_kids_with_present = cookies(count_of_presents, nice_kids_with_present)

    neighbourhood[santa_start_position[0]][santa_start_position[1]] = "-"

    if not count_of_presents or nice_kids_with_present == total_nice_kids:
        break

    command_line = input()

neighbourhood[santa_start_position[0]][santa_start_position[1]] = "S"

if not count_of_presents and nice_kids_with_present < total_nice_kids:
    print("Santa ran out of presents!")

[print(*row) for row in neighbourhood]

if nice_kids_with_present == total_nice_kids:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - nice_kids_with_present} nice kid/s.")
