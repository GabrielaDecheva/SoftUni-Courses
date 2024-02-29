from project.guild import Guild
from project.player import Player

player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
player_two = Player("Tom", 50, 100)
guild_two = Guild("test")
print(guild_two.assign_player(player_two))
print(guild.assign_player(player_two))
print(guild.kick_player("George"))

print(guild.guild_info())