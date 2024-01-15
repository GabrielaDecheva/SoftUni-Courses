n = int(input())
elements = set()
for _ in range(n):
    for el in input().split():
        elements.add(el)
print(*elements, sep="\n")

