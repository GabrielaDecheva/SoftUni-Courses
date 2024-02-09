def team_lineup(*football_players_info):
    players_dict = {}
    result = ""
    for info in football_players_info:
        name, country = info[0], info[1]
        if country not in players_dict.keys():
            players_dict[country] = []
        players_dict[country] += [name]

    sorted_result = sorted(players_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    for country, footballers in sorted_result:
        result += f"{country}:\n"
        for player in footballers:
            result += f"  -{player}\n"

    return result


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))

