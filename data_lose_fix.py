import re

file = open("logs.txt", "r")
data = file.readlines()
emeralds = {}
stat = {}
kill = {}
pvp_death = {}

for line in data:
    # if re.search("Removed \d+ items from player .+", line):
    #     number = int(re.search("Removed (\d+) items from player .+", line).group(1))
    #     player = re.search("Removed \d+ items from player (.+)", line).group(1)
    #     if player in emeralds.keys():
    #         emeralds[player] += number
    #     else:
    #         emeralds[player] = number
    # if re.search("perd \d+ Ã©meraudes", line):
    #     number = int(re.search(".* perd (\d+) Ã©meraudes", line).group(1))
    #     player = re.search("(.*) perd \d+ Ã©meraudes", line).group(1)
    #     if player in emeralds.keys():
    #         emeralds[player] -= number
    #     else:
    #         emeralds[player] = -number
    # if re.search("] Â§x.+ est mort par", line):
    #     player = re.search("] Â§x(.+) est mort par", line).group(1)
    #     if player in stat.keys():
    #         stat[player] += 1
    #     else:
    #         stat[player] = 1
    #print(line)
    if re.search("\] Â§x.+ a tuÃ© \[Â§x.+\] Â§x.+ avec ", line):
        killer = re.search("\] Â§x(.+) a tuÃ© \[Â§x.+\] Â§x.+ avec ", line).group(1)
        victim = re.search("\] Â§x.+ a tuÃ© \[Â§x.+\] Â§x(.+) avec ", line).group(1)
        if killer in kill.keys():
            kill[killer] += 1
        else:
            kill[killer] = 1
        if victim in pvp_death.keys():
            pvp_death[victim] += 1
        else:
            pvp_death[victim] = 1


#for player in emeralds.keys():
#    print(player, emeralds[player])
# for player in stat.keys():
#     print("*skript*add "+str(stat[player])+" to {cw.death.pve::"+player+"}")
for player in kill.keys():
    print("*skript*add "+str(kill[player])+" to {cw.death.kill::"+player+"}")
print("morts:")
for player in pvp_death.keys():
    print("*skript*add "+str(pvp_death[player])+" to {cw.death.tue::"+player+"}")
