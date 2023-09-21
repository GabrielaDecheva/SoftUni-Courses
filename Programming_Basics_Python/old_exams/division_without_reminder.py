n = int(input())
p1 = 0
p2 = 0
p3 = 0

for _ in range(n):
    number = int(input())
    if number % 2 == 0:
        p1 += 1
    if number % 3 == 0:
        p2 += 1
    if number % 4 == 0:
        p3 += 1

p1_percentage = p1 / n * 100
p2_percentage = p2 / n * 100
p3_percentage = p3 / n * 100

print(f'{p1_percentage:.2f}%')
print(f'{p2_percentage:.2f}%')
print(f'{p3_percentage:.2f}%')