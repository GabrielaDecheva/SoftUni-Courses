row, coll = [int(x) for x in input().split(", ")]

total_sum = 0
matrix = []

for i in range(row):
    data = [int(el) for el in input().split(", ")]
    total_sum += sum(data)
    matrix.append(data)

print(total_sum)
print(matrix)