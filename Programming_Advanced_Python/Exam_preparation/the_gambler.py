size_of_board = int(input())
initial_amount = 100
gambler_position = []
matrix_board = []
flag_out_of_range = False

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size_of_board):
    current_row = list(input())
    matrix_board.append(current_row)

    if "G" in matrix_board[row]:
        gambler_position = [row, matrix_board[row].index("G")]
        matrix_board[gambler_position[0]][gambler_position[1]] = "-"

command_line = input()
while command_line != "end":
    gambler_position = [
        gambler_position[0] + directions[command_line][0],
        gambler_position[1] + directions[command_line][1]
    ]
    r, c = gambler_position

    if not 0 <= r < size_of_board and 0 <= c < size_of_board:
        flag_out_of_range = True
        break

    if matrix_board[r][c] == "-":
        command_line = input()
        continue
    elif matrix_board[r][c] == "W":
        initial_amount += 100
        matrix_board[r][c] = "-"
    elif matrix_board[r][c] == "P":
        initial_amount -= 200
        if initial_amount <= 0:
            break
    elif matrix_board[r][c] == "J":
        initial_amount += 100000
        break
    command_line = input()

matrix_board[gambler_position[0]][gambler_position[1]] = "G"

if flag_out_of_range or initial_amount <= 0:
    print("Game over! You lost everything!")
elif initial_amount >= 100000:
    print("You win the Jackpot!")
    print(f"End of the game. Total amount: {initial_amount}$")
else:
    print(f"End of the game. Total amount: {initial_amount}$")

if initial_amount > 0:
    for row in matrix_board:
        print(*row, sep="")
