# def check_boundaries(matrix_r, matrix_c, row, col):
#     if 0 <= row < matrix_r and 0 <= col < matrix_c:
#         return True
#     return False
#
#
# rows, cols = [int(x) for x in input().split()]
# neighborhood = []
# start_boy_position = None
#
# directions = {
#     "up": (-1, 0),
#     "down": (1, 0),
#     "left": (0, -1),
#     "right": (0, 1),
# }
#
# for row in range(rows):
#     neighborhood.append(list(input()))
#     if "B" in neighborhood[row]:
#         start_boy_position = (row, neighborhood[row].index("B"))
#
# current_boy_position = start_boy_position
#
# while True:
#     command = input()
#     new_row, new_col = current_boy_position[0] + directions[command][0], current_boy_position[1] + directions[command][1]
#     if not check_boundaries(rows, cols, new_row, new_col):
#         print ("The delivery is late. Order is canceled.")
#         neighborhood[start_boy_position[0]][start_boy_position[1]] = " "
#         break
#     if neighborhood[new_row][new_col] == "P":
#         neighborhood[new_row][new_col] = "R"
#         current_boy_position = [new_row, new_col]
#         print("Pizza is collected. 10 minutes for delivery.")
#     elif neighborhood[new_row][new_col] == "-":
#         current_boy_position = [new_row, new_col]
#         neighborhood[new_row][new_col] = "."
#     elif neighborhood[new_row][new_col] == ".":
#         current_boy_position = [new_row, new_col]
#     elif neighborhood[new_row][new_col] == "B":
#         current_boy_position = [new_row, new_col]
#     elif neighborhood[new_row][new_col] == "A":
#         neighborhood[new_row][new_col] = "P"
#         print("Pizza is delivered on time! Next order...")
#         break
#     elif neighborhood[new_row][new_col] == "*":
#         continue
#
#
# for row in neighborhood:
#     print(*row, sep="")

def is_in_scope(row_index, col_index, row_count, col_count):
    return 0 <= row_index < row_count and 0 <= col_index < col_count


direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


n, m = [int(el) for el in input().split()]

matrix = []
initial_position = None

for row_index in range(n):
    data = list(input())

    if "B" in data:
        col_index = data.index("B")
        initial_position = (row_index, col_index)
    matrix.append(data)


current_position = initial_position

while True:
    direction = input()

    current_row_index, current_col_index = current_position
    row_movement, col_movement = direction_mapper[direction]
    desired_row = current_row_index + row_movement
    desired_col = current_col_index + col_movement

    if not is_in_scope(desired_row, desired_col, n, m):
        matrix[initial_position[0]][initial_position[1]] = " "
        print(f"The delivery is late. Order is canceled.")
        break

    symbol = matrix[desired_row][desired_col]

    if symbol == "*":
        continue

    current_position = [desired_row, desired_col]

    if symbol == "P":
        print(f"Pizza is collected. 10 minutes for delivery.")
        matrix[desired_row][desired_col] = "R"

    elif symbol == "A":
        matrix[desired_row][desired_col] = "P"
        print(f"Pizza is delivered on time! Next order...")
        break

    elif symbol == "-":
        matrix[desired_row][desired_col] = "."


for row in matrix:
    print(''.join(row))