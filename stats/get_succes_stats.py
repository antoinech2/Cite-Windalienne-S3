import re

file = open("sucess.txt", "r")
data = file.readlines()

players_number = {}
players_emeralds = {}
equipe_number = {}
equipe_emeralds = {}

total_emerald = 0
for line in data:
    player = re.search("\] \[Â§x.+\] Â§x(.+) gagne \d+ Ã©meraudes pour la rÃ©alisation de son succÃ¨s !", line).group(1)
    team = re.search("\] \[Â§x(.+)\] Â§x.+ gagne \d+ Ã©meraudes pour la rÃ©alisation de son succÃ¨s !", line).group(1)
    emeralds = int(re.search("\] \[Â§x.+\] Â§x.+ gagne (\d+) Ã©meraudes pour la rÃ©alisation de son succÃ¨s !", line).group(1))
    total_emerald += emeralds
    if player in players_number.keys():
        players_number[player] += 1
    else:
        players_number[player] = 1
    if player in players_emeralds.keys():
        players_emeralds[player] += emeralds
    else:
        players_emeralds[player] = emeralds
    if team in equipe_number.keys():
        equipe_number[team] += 1
    else:
        equipe_number[team] = 1
    if team in equipe_emeralds.keys():
        equipe_emeralds[team] += emeralds
    else:
        equipe_emeralds[team] = emeralds
    print(team, player, emeralds)

players_number = {k: v for k, v in sorted(players_number.items(), key=lambda item: item[1], reverse=True)}
players_emeralds = {k: v for k, v in sorted(players_emeralds.items(), key=lambda item: item[1], reverse=True)}
equipe_number = {k: v for k, v in sorted(equipe_number.items(), key=lambda item: item[1], reverse=True)}
equipe_emeralds = {k: v for k, v in sorted(equipe_emeralds.items(), key=lambda item: item[1], reverse=True)}

number = 1
for player in players_number.keys():
    print("{}ème : {} ({})".format(number, player, players_number[player]))
    number += 1

number = 1
for player in players_emeralds.keys():
    print("{}ème : {} ({})".format(number, player, players_emeralds[player]))
    number += 1

number = 1
for player in equipe_number.keys():
    print("{}ème : {} ({})".format(number, player, equipe_number[player]))
    number += 1

number = 1
for player in equipe_emeralds.keys():
    print("{}ème : {} ({})".format(number, player, equipe_emeralds[player]))
    number += 1

print(total_emerald)
