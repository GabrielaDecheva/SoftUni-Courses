row_count = int(input())
matrix =[]
for i in range(row_count):
    data = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    matrix.append(data)

print(matrix)
