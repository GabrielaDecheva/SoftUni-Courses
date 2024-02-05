from collections import deque

initial_fuel = [int(x) for x in input().split()]
add_consumption_index = deque(int(x) for x in input().split())
needed_amount_of_fuel = deque(int(x) for x in input().split())

reached_altitudes = []
altitude = 1
reached = True

while initial_fuel:
    current_fuel = initial_fuel.pop()
    current_index = add_consumption_index.popleft()
    result = current_fuel - current_index
    if result >= needed_amount_of_fuel.popleft():
        print(f"John has reached: Altitude {altitude}")
        reached_altitudes.append(altitude)
    else:
        reached = False
        print(f"John did not reach: Altitude {altitude}")
        print("John failed to reach the top.")
        break
    altitude += 1

if not reached and len(reached_altitudes) > 0:
    reached_altitude_as_str = ', '.join(f"Altitude {x}" for x in reached_altitudes)
    print(f"Reached altitudes: {reached_altitude_as_str}")
elif not reached and not reached_altitudes:
    print("John didn't reach any altitude.")
else:
    print("John has reached all the altitudes and managed to reach the top!")