def valid_index(row, col, matrix_row, matrix_col):
    if 0 <= row < matrix_row and 0 <= col < matrix_col:
        return True
    return False


rows, cols = [int(x) for x in input().split(",")]
cupboard = []
total_cheese = 0
eaten_cheese = 0
current_mouse_position = []
last_command = ""
danger_flag = False


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(rows):
    cupboard.append(list(input()))
    if "M" in cupboard[row]:
        current_mouse_position = [row, cupboard[row].index("M")]
        cupboard[row][current_mouse_position[1]] = "*"
    total_cheese += cupboard[row].count("C")


while True:
    command = input()

    if command == "danger":
        cupboard[current_mouse_position[0]][current_mouse_position[1]] = "M"
        danger_flag = True
        break

    next_row = current_mouse_position[0] + directions[command][0]
    next_col = current_mouse_position[1] + directions[command][1]
    if not valid_index(next_row, next_col, rows, cols):
        cupboard[current_mouse_position[0]][current_mouse_position[1]] = "M"
        print("No more cheese for tonight!")
        break
    if cupboard[next_row][next_col] == "C":
        current_mouse_position = [next_row, next_col]
        cupboard[next_row][next_col] = "*"
        eaten_cheese += 1
        if eaten_cheese == total_cheese:
            cupboard[next_row][next_col] = "M"
            print("Happy mouse! All the cheese is eaten, good night!")
            break
    elif cupboard[next_row][next_col] == "*":
        current_mouse_position = [next_row, next_col]
    elif cupboard[next_row][next_col] == "@":
        continue
    elif cupboard[next_row][next_col] == "T":
        cupboard[next_row][next_col] = "M"
        print("Mouse is trapped!")
        break

if danger_flag and eaten_cheese < total_cheese:
    print("Mouse will come back later!")

for row in cupboard:
    print(*row, sep="")
