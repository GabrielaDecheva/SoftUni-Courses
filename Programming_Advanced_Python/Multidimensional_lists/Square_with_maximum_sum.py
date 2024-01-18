row, col = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(row):
    matrix.append([int(el) for el in input().split(", ")])

max_sum = float("-inf")
sub_matrix = []

for row_index in range(row - 1):
    for col_index in range(col - 1):
        curr_element = matrix[row_index][col_index]
        next_el = matrix[row_index][col_index + 1]
        below_el = matrix[row_index + 1][col_index]
        diagonal_el = matrix[row_index + 1][col_index + 1]

        total_sum = curr_element + next_el + below_el + diagonal_el

        if max_sum < total_sum:
            max_sum = total_sum
            sub_matrix = [[curr_element, next_el], [below_el, diagonal_el]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)