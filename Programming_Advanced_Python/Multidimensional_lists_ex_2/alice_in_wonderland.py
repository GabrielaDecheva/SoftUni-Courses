size = int(input())

matrix = []
alise_pos = []

tea_bags = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(input().split())
    if "A" in matrix[row]:
        alise_pos = [row, matrix[row].index("A")]
        matrix[row][alise_pos[1]] = "*"

while tea_bags < 10:
    direction = input()

    row = alise_pos[0] + directions[direction][0]
    col = alise_pos[1] + directions[direction][1]

    if not (0 <= row < size and 0 <= col < size):
        break

    alise_pos = [row, col]
    element_found = matrix[row][col]
    matrix[row][col] = '*'

    if element_found == "R":
        break

    if element_found.isdigit():
        tea_bags += int(element_found)

if tea_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")
[print(*row) for row in matrix]


