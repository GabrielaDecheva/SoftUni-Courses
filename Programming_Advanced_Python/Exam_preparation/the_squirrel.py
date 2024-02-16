from collections import deque


def valid_index(size, row, col):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


size = int(input())
commands = deque(input().split(", "))
field = []
squirrel_pos = []
collected_hazelnuts = 0
trap_flag = False
win_flag = False

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    field.append(list(input()))
    if "s" in field[row]:
        squirrel_pos = [row, field[row].index("s")]
        field[squirrel_pos[0]][squirrel_pos[1]] = "*"


while commands:
    current_command = commands.popleft()
    new_row = squirrel_pos[0] + directions[current_command][0]
    new_col = squirrel_pos[1] + directions[current_command][1]
    if not valid_index(size, new_row, new_col):
        print("The squirrel is out of the field.")
        break
    squirrel_pos = [new_row, new_col]
    symbol = field[squirrel_pos[0]][squirrel_pos[1]]
    if symbol == "h":
        collected_hazelnuts += 1
        if collected_hazelnuts == 3:
            win_flag = True
            print("Good job! You have collected all hazelnuts!")
            break
        field[squirrel_pos[0]][squirrel_pos[1]] = "*"
    elif symbol == "t":
        trap_flag = True
        print("Unfortunately, the squirrel stepped on a trap...")
        break

    if not commands:
        print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {collected_hazelnuts}")
