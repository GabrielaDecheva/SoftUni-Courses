group = int(input())
days = int(input())

companions = group
coins = 0

for day in range(1, days + 1):
    if day % 10 == 0:
        companions -= 2
    if day % 15 == 0:
        companions += 5
    if day % 3 == 0:
        coins -= 3 * companions
    if day % 5 == 0:
        coins += 20 * companions
        if day % 3 == 0:
            coins -= 2 * companions
    coins += 50
    coins -= companions * 2

print(f'{companions} companions received {int(coins / companions)} coins each.')