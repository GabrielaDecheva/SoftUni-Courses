names_count = int(input())
names = set()

for _ in range(names_count):
    names.add(input())

print(*names, sep="\n")


# 2

# print(*{input() for _ in range(int(input()))}, sep="\n")