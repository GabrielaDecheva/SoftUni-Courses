rows, cols = [int(el) for el in input().split()]

letter = ord("a")

for row in range(letter, rows + letter):
    for col in range(row, row + cols):
        current_line = chr(row) + chr(col) + chr(row)
        print(current_line, sep=" ", end=' ')
    print()