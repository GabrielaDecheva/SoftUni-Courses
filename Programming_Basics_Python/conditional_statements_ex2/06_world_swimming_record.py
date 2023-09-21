import math

world_record = float(input())
distance_meters = float(input())
seconds_per_meter = float(input())

total_time_in_sec = distance_meters * seconds_per_meter

delay_in_sec = math.floor(distance_meters / 15) * 12.5

total_with_delay = total_time_in_sec + delay_in_sec

diff_time = abs(total_with_delay - world_record)

if total_with_delay < world_record:
    print(f'Yes, he succeeded! The new world record is {total_with_delay:.2f} seconds.')
if total_with_delay >= world_record:
    print(f'No, he failed! He was {diff_time:.2f} seconds slower.')