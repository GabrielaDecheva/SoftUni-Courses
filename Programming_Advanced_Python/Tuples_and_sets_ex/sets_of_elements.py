set_one, set_two = [int(x) for x in input().split()]
first = set()
second = set()
for _ in range(set_one):
    first.add(int(input()))
    #first = {input() for _ in range(set_one)}

for _ in range(set_two):
    second.add(int(input()))

print(*first.intersection(second), sep="\n")

