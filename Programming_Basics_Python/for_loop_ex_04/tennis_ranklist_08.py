count_games = int(input())
initial_points = int(input())

W = 0
F = 0
SF = 0

for _ in range(count_games):
    current_game = input()
    if current_game == 'W':
        W += 1
    elif current_game == 'F':
        F += 1
    elif current_game == 'SF':
        SF += 1

total_points = initial_points + (W * 2000) + (F * 1200) + (SF * 720)
average_points = int((total_points - initial_points) / count_games)
percent_wins = (W / count_games) * 100

print(f'Final points: {total_points}')
print(f'Average points: {average_points}')
print(f'{percent_wins:.2f}%')