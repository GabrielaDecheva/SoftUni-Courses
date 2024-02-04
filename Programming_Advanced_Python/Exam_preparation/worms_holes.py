from collections import deque

worms = [int(x) for x in input().split()]
holes = deque(int(x) for x in input().split())

matches = 0
zero_valued_worms = 0

while worms and holes:
    current_worm = worms[-1]
    current_hole = holes.popleft()

    if current_hole == current_worm:
        worms.pop()
        matches += 1
    else:
        worms[-1] -= 3
        if worms[-1] <= 0:
            worms.pop()
            zero_valued_worms += 1

if matches:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")


if not worms and zero_valued_worms > 0:
    print("Worms left: none")
elif not worms and zero_valued_worms == 0:
    print("Every worm found a suitable hole!")
if worms:
    print(f"Worms left: {', '.join(str(worm) for worm in worms)}" )

if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join(str(hole) for hole in holes)}")
