row = int(input())

flatten_matrix = []

for i in range(row):
    row_data = [int(el) for el in input().split(", ")]
    for el in row_data:
        flatten_matrix.append(el)
    #flatten_matrix.extend(row_data) -> unpack el from list and append to a new list
print(flatten_matrix)