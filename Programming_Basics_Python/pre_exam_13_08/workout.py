import math

days_running = int(input())
km_first_day = float(input())

km_running = km_first_day
all_km = 0

for _ in range (days_running):
    percent_over_first_day = int(input())
    km_running = km_running + (km_running * percent_over_first_day / 100)
    all_km += km_running

total_km_all_days = all_km + km_first_day

diff = math.ceil(abs(total_km_all_days - 1000))

if total_km_all_days >= 1000:
    print(f"You've done a great job running {diff} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {diff} more kilometers")
