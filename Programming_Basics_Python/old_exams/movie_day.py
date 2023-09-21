time_for_shoot = int(input())
count_scenes = int(input())
duration_per_scene = int(input())

prep_decor = time_for_shoot * 0.15
total_shooting_time = count_scenes * duration_per_scene
total_time_needed = prep_decor + total_shooting_time

diff = round(abs(time_for_shoot - total_time_needed))
if time_for_shoot >= total_time_needed:
    print(f'You managed to finish the movie on time! You have {diff} minutes left!')
elif time_for_shoot < total_time_needed:
    print(f'Time is up! To complete the movie you need {diff} minutes.')