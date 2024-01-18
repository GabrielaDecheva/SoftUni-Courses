row = int(input())
matrix = []

for _ in range(row):
    data = [el for el in input()]
    matrix.append(data) # matrix.append(list(input())

searched_element = input()
is_found = False

for row_index in range(row):
    if is_found:
        break
    for col_index in range(len(matrix[row_index])):
        if matrix[row_index][col_index] == searched_element:
            print(f"({row_index}, {col_index})")
            is_found = True
            break
            #exit -> without the boolean and instead of break

if not is_found:
    print(f"{searched_element} does not occur in the matrix")