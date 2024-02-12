# def check_boundaries(matrix_r, matrix_c, row, col):
#     if 0 <= row < matrix_r and 0 <= col < matrix_c:
#         return True
#     return False
#
#
# rows, cols = [int(x) for x in input().split()]
# neighborhood = []
# start_boy_position = []
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
#         start_boy_position = [row, neighborhood[row].index("B")]
#
# current_boy_position = start_boy_position
#
# while True:
#     command = input()
#     new_row, new_col = current_boy_position[0] + directions[command][0], current_boy_position[1] + directions[command][1]
#     if check_boundaries(rows, cols, new_row, new_col):
#         if neighborhood[new_row][new_col] == "P":
#             neighborhood[new_row][new_col] = "R"
#             current_boy_position = [new_row, new_col]
#             print("Pizza is collected. 10 minutes for delivery.")
#         elif neighborhood[new_row][new_col] == "-":
#             current_boy_position = [new_row, new_col]
#             neighborhood[new_row][new_col] = "."
#         elif neighborhood[new_row][new_col] == "A":
#             neighborhood[new_row][new_col] = "P"
#             print("Pizza is delivered on time! Next order...")
#             break
#         elif neighborhood[new_row][new_col] == "*":
#             continue
#     else:
#         print("The delivery is late. Order is canceled.")
#         neighborhood[start_boy_position[0]][start_boy_position[1]] = " "
#         break
#
# for row in neighborhood:
#     print(*row, sep="")
#


def check_boundaries(matrix_r, matrix_c, row, col):
    if 0 <= row < matrix_r and 0 <= col < matrix_c:
        return True
    return False


rows, cols = [int(x) for x in input().split()]
neighborhood = []
start_boy_position = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(rows):
    neighborhood.append(list(input()))
    if "B" in neighborhood[row]:
        start_boy_position = [row, neighborhood[row].index("B")]

current_boy_position = start_boy_position

while True:
    command = input()
    new_row, new_col = current_boy_position[0] + directions[command][0], current_boy_position[1] + directions[command][1]
    if not check_boundaries(rows, cols, new_row, new_col):
        print("The delivery is late. Order is canceled.")
        neighborhood[start_boy_position[0]][start_boy_position[1]] = " "
        break
    if neighborhood[new_row][new_col] == "P":
        neighborhood[new_row][new_col] = "R"
        current_boy_position = [new_row, new_col]
        print("Pizza is collected. 10 minutes for delivery.")
    elif neighborhood[new_row][new_col] == "-":
        current_boy_position = [new_row, new_col]
        neighborhood[new_row][new_col] = "."
    elif neighborhood[new_row][new_col] == ".":
        current_boy_position = [new_row, new_col]
    elif neighborhood[new_row][new_col] == "B":
        current_boy_position = [new_row, new_col]
    elif neighborhood[new_row][new_col] == "A":
        neighborhood[new_row][new_col] = "P"
        print("Pizza is delivered on time! Next order...")
        break
    elif neighborhood[new_row][new_col] == "*":
        continue


for row in neighborhood:
    print(*row, sep="")
