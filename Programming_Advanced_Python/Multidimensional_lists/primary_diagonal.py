row = int(input())

matrix = []

for _ in range(row):
    matrix.append([int(el) for el in input().split()])

diagonal = 0
for row_index in range(row):
    # diagonal += matrix[row_index][row_index] -> instead the next 3 lines
    for col_index in range(row):
        if row_index == col_index:
            diagonal += matrix[row_index][col_index]
print(diagonal)

