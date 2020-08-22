import re

file = open("logs.txt", "r")
data = file.readlines()

players_emeralds = {}
total = 0
total_emerald = 0
for line in data:
    if re.search("perd \d+ Ã©meraudes", line):
        player = re.search("(.+) perd \d+ Ã©meraudes", line).group(1)
        emeralds = int(re.search(".+ perd (\d+) Ã©meraudes", line).group(1))
        total += emeralds
        total_emerald += emeralds
        if player in players_emeralds.keys():
            players_emeralds[player] += emeralds
        else:
            players_emeralds[player] = emeralds

players_emeralds = {k: v for k, v in sorted(players_emeralds.items(), key=lambda item: item[1], reverse=True)}

number = 1
for player in players_emeralds.keys():
    print("{}ème : {} ({})".format(number, player, players_emeralds[player]))
    number += 1

print(players_emeralds)
