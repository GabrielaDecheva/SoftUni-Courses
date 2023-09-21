name_of_team = input()
count_games = int(input())
w = 0
d = 0
l = 0
w_points = 3
d_points = 1
for i in range(count_games):
    result = input()
    if result == 'W':
        w += 1
    elif result == 'D':
        d += 1
    elif result == 'L':
        l += 1

if count_games < 1:
    print(f"{name_of_team} hasn't played any games during this season.")
else:
    total_points = (w * w_points) + (d * d_points)
    win_rate = w / count_games * 100
    print(f'{name_of_team} has won {total_points} points during this season.')
    print('Total stats:')
    print(f'## W: {w}')
    print(f'## D: {d}')
    print(f'## L: {l}')
    print(f'Win rate: {win_rate:.2f}%')
