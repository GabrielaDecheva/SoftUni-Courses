from collections import deque

armour_of_monsters = deque(int(num) for num in input().split(","))
soldiers_strength = [int(num) for num in input().split(",")]

monsters_killed = 0

while True:
    current_monster = armour_of_monsters.popleft()
    current_soldier = soldiers_strength.pop()

    if current_soldier >= current_monster:
        monsters_killed += 1
        strength_left = current_soldier - current_monster
        if soldiers_strength and strength_left > 0:
            soldiers_strength[-1] += strength_left
        elif not soldiers_strength and strength_left > 0:
            soldiers_strength.append(strength_left)

    elif current_monster > current_soldier:
        strength_left = current_monster - current_soldier
        armour_of_monsters.append(strength_left)

    if not soldiers_strength or not armour_of_monsters:
        break

if not armour_of_monsters:
    print("All monsters have been killed!")

if not soldiers_strength:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {monsters_killed}")
