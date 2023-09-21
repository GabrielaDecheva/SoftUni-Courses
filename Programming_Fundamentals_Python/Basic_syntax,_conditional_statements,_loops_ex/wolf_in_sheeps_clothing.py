string = input()
herd = string.split(", ")
if herd[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    herd_count = len(herd)
    wolf_index = herd.index("wolf")
    sheep_in_danger_index = (len(herd) - 1) - wolf_index
    print(f"Oi! Sheep number {sheep_in_danger_index}! You are about to be eaten by a wolf!")