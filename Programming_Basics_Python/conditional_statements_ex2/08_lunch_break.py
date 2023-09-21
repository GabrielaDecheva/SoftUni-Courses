import math

name_of_movie = input()
length_of_movie = int(input())
length_of_break = int(input())

lunch_time = length_of_break / 8
relax_time = length_of_break / 4
time_left = length_of_break - (lunch_time + relax_time)

diff = math.ceil(abs(time_left - length_of_movie))

if time_left >= length_of_movie:
    print(f'You have enough time to watch {name_of_movie} and left with {diff} minutes free time.')
else:
    print(f"You don't have enough time to watch {name_of_movie}, you need {diff} more minutes.")