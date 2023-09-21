name_of_actor = input()
initial_points = float(input())
count_jury = int(input())

total_jury_points = 0

for _ in range(count_jury):
    name_of_jury = input()
    points = float(input())
    total_jury_points += (len(name_of_jury) * points) / 2

    if total_jury_points + initial_points > 1250.5:
        print(f'Congratulations, {name_of_actor} got a nominee for leading role with {total_jury_points + initial_points:.1f}!')
        break

else:
    diff = 1250.5 - (total_jury_points + initial_points)
    print(f'Sorry, {name_of_actor} you need {diff:.1f} more!')
