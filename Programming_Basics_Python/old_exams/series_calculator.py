import math

name_of_series = input()
count_seasons = int(input())
count_episodes = int(input())
duration_per_episode = float(input())

commercials = duration_per_episode * 0.2
duration_episode_with_comm = duration_per_episode + commercials
additional_mins = count_seasons * 10
total_time = math.floor((duration_episode_with_comm * count_episodes) * count_seasons) + additional_mins

print(f"Total time needed to watch the {name_of_series} series is {total_time} minutes.")