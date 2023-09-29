cards_list = input().split()
game_terminated = False
team_a = []
team_b = []

for card in cards_list:
    if "A" in card and card not in team_a:
        team_a.append(card)
    elif "B" in card and card not in team_b:
        team_b.append(card)
    if len(team_a) > 4 or len(team_b) > 4:
        game_terminated = True
        break

print(f"Team A - {11 - len(team_a)}; Team B - {11 - len(team_b)}")
if game_terminated:
    print("Game was terminated")
