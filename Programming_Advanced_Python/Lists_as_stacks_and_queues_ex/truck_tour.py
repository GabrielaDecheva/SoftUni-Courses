from collections import deque

gas_station_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])

gas_station_data_copy = gas_station_data.copy()
gas_in_tank = 0
index = 0

while gas_station_data_copy:
    petrol, distance = gas_station_data_copy.popleft()

    gas_in_tank += petrol

    if gas_in_tank >= distance:
        gas_in_tank -= distance
    else:
        gas_station_data.rotate(-1) # left to right
        gas_station_data_copy = gas_station_data.copy()
        index += 1
        gas_in_tank = 0

print(index)