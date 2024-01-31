import os

name = "numbers.txt"
file = open(name)
total_sum = 0
for line in file.readlines():
    total_sum += int(line.strip())

print(total_sum)