size = int(input())
matrix = [list(input()) for _ in range(size)]

# pos_nums = [-2, -1, 1, 2]
#positions = [(x, y) for x in pos_nums for y in pos_nums if abs(x) != abs(y)]
positions = (
    (-2, -1), #горе 2, ляво 1
    (-2, 1), #горе 2, дясно 1
    (-1, -2), #горе 1, ляво 2
    (-1, 2), #горе 1, дясно 2
    (2, 1), #долу 2, дясно 1
    (2, -1), #долу 2, ляво 1
    (1, -2),#долу 1, ляво 2
    (1, 2), #долу 1, ляво 2
)

removed_knights = 0

while True:
    max_attacks = 0
    most_attacks_position = [] # row, col

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 'K':
                attacks = 0

                for pos in positions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < size and 0 <= pos_col < size:
                        if matrix[pos_row][pos_col] == 'K':
                            attacks += 1
                if attacks > max_attacks:
                    most_attacks_position = [row, col]
                    max_attacks = attacks

    if most_attacks_position:
        r, c = most_attacks_position
        matrix[r][c] = "0"
        removed_knights += 1
    else:
        break
print(removed_knights)