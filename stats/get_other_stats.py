#from JsonGet import json_get, json_get_default, JList
import json

stats = {} #Données à entrée, joueur : valeur

equipes = {"OUI" : ["CodeCubes", "Valaack", "Maxharance", "FONCEUR59"], "LesPapas" : ["0xilia", "_Le_Joker", "Seaks89", "KindEd"], "4-AstrophE" : ["titouz41", "ely_on", "Hissney", "Yumelia"], "NYAAAAAAAA" : ["antoinech", "Toutankhamon", "Kiillua_", "Rajalaxx"], "Extellia" : ["TurnHour", "Bennyboyrools", "Hukatio", "kiven532"], "NoName" : ["Faaela", "Lekalite", "BountyGames", "zelda_jojo_2001"], "DoggyStyle" : ["Zezor", "Amex92i5137", "LeDouxPoete", "Crowning"], "4-Peccable" :["LaTartOP0ireS_", "Akcno", "BabyDiscoPanda", "Caypepsi"]}

stat_sorted = {k: v for k, v in sorted(stats.items(), key=lambda item: item[1], reverse=True)}

number = 1
for player in stat_sorted.keys():
    value = stat_sorted[player]
    #result = json_get(json, json_path)
    print("{}ème : {} ({})".format(number, player, value))
    number += 1

team_stat = {}
total_time = 0
for equipe in equipes.keys():
    value = 0
    for player in equipes[equipe]:
        if player in stats.keys():
            value += stat_sorted[player]
    team_stat[equipe] = value
    total_time += value
team_stat_sorted = {k: v for k, v in sorted(team_stat.items(), key=lambda item: item[1], reverse=True)}

number = 1
for equipe in team_stat_sorted.keys():
    value = team_stat_sorted[equipe]
    print("{}ème : {} ({})".format(number, equipe, value))
    number += 1

print(total_time)
