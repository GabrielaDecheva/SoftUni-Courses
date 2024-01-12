clothes = [int(x) for x in input().split()]
shelf_space = int(input())

shelves = 1
current_shelf_space = shelf_space

while clothes:
    cloth = clothes.pop()

    if current_shelf_space >= cloth:
        current_shelf_space -= cloth
    else:
        shelves += 1
        current_shelf_space = shelf_space - cloth
print(shelves)