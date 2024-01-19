rows, cols = [int(el) for el in input().split()]
matrix = []
# matrix = [input().split() for _ in range(rows)]
count_matches = 0

for _ in range(rows):
    data = input().split()
    matrix.append(data)

for row in range(rows - 1):
    for col in range(cols - 1):
        symbol = matrix[row][col]

        if symbol == matrix[row][col + 1] and symbol == matrix[row + 1][col] and symbol == matrix[row + 1][col + 1]:
            count_matches += 1

print(count_matches)