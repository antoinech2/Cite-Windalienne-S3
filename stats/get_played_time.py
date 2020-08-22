#from JsonGet import json_get, json_get_default, JList
import json

uuids = {"0xilia" : "c1e73946-0d4a-342b-92a2-db24e7dea11f", "_Le_Joker" : "6c45854a-973d-3d13-8662-fa5b9825d365", "Akcno" : "eb139271-4a00-38e2-86c3-831507efafd5", "Amex92i5137" : "d0f92b42-e43f-3f2d-98af-f3f9a7041dad", "antoinech" : "25018273-71f2-3439-89e2-0c3a98f8abd3", "BabyDiscoPanda" : "bd3aad9a-f11f-3f84-91ce-526aaf91dfa2", "Bennyboyrools" : "474ce0aa-35ef-341f-85d0-a7ed8d179c1e", "BountyGames" : "8f23c84c-e4a6-3404-887a-89707b043541", "Caypepsi" : "b0ea6b09-39c8-3cb1-99e9-fe01ef8ea50a", "CodeCubes" : "6091754a-3c0f-3e38-a642-4ab889a8df96", "Crowning" : "8a97c348-c734-3f3a-b38a-fec983ab2fba", "ely_on" : "7fc0e3e8-999e-3735-8782-e85bbeb69f48", "Faaela" : "f075a918-aa07-3b42-bbc3-16757b180831", "FONCEUR59" : "e60d4c4a-1c96-3d20-9861-09fe5ddc3483", "Hissney" : "6e615079-7c62-3065-ae8c-37f37e4f7fe7", "Hukatio" : "7dd51782-031d-3984-8af3-d00268b9302c", "Kiillua_" : "39addacb-ccdc-35cd-b8c6-cda460be4cd9", "KindEd" : "c98d6ebf-1ba0-3fc9-9adf-72f729319e3d", "kiven532" : "0233e4be-9e3c-313d-a18c-a30638711dab", "LaTartOP0ireS_" : "9b9921e5-4885-3950-828c-f7db4871f1fb", "LeDouxPoete" : "d1638fbc-0d5c-3fa4-84fe-f124f300d076", "Lekalite" : "af59af2c-c303-3823-9d8c-19141ba6fb83", "Maxharance" : "dd1b5645-09e9-3737-aeb6-fb52dd15d2bd", "Rajalaxx" : "2641df5b-f7d9-38a4-8250-ca3651560387", "Seaks89" : "afd35e68-d7d6-3fb5-8832-d8d9739d994c", "titouz41" : "015c1d6e-fe6e-35b6-b32c-37e5fec807c8", "Toutankhamon" : "9813b59f-0d34-3be2-a55a-c15044ecc032", "TurnHour" : "165f8056-97e2-3ac2-bd65-b0eac532927e", "Valaack" : "c3148070-7681-3e6b-a4d9-26617d9781a0", "Yumelia" : "ed4379b4-7896-3465-8b00-ccdde6690df4", "zelda_jojo_2001" : "8dd07277-338d-3aee-97f6-e0413856087b", "Zezor" : "d02fe7cf-3334-3262-937e-7093f4512f65"}

equipes = {"OUI" : ["CodeCubes", "Valaack", "Maxharance", "FONCEUR59"], "LesPapas" : ["0xilia", "_Le_Joker", "Seaks89", "KindEd"], "4-AstrophE" : ["titouz41", "ely_on", "Hissney", "Yumelia"], "NYAAAAAAAA" : ["antoinech", "Toutankhamon", "Kiillua_", "Rajalaxx"], "Extellia" : ["TurnHour", "Bennyboyrools", "Hukatio", "kiven532"], "NoName" : ["Faaela", "Lekalite", "BountyGames", "zelda_jojo_2001"], "DoggyStyle" : ["Zezor", "Amex92i5137", "LeDouxPoete", "Crowning"], "4-Peccable" :["LaTartOP0ireS_", "Akcno", "BabyDiscoPanda", "Caypepsi"]}

time = {}

for player in uuids:
    uuid = uuids[player]
    filename = "stats/"+uuid+".json"
    file = open(filename, "r")
    data = file.read()
    json_data = json.loads(data)
    result = 0
    result = int(json_data["stats"]["minecraft:custom"]["minecraft:play_one_minute"])/1200
    print(result)
    file.close()

    time[player] = result

time_sorted = {k: v for k, v in sorted(time.items(), key=lambda item: item[1], reverse=True)}

number = 1
for player in time_sorted.keys():
    result = time_sorted[player]
    #result = json_get(json, json_path)
    hours = int(result//60)
    mins = round(result%60)
    print("{}ème : {} ({}h {}min)".format(number, player, hours, mins))
    number += 1

team_time = {}
total_time = 0
for equipe in equipes.keys():
    time = 0
    for player in equipes[equipe]:
        time += time_sorted[player]
    team_time[equipe] = time
    total_time += time
team_time_sorted = {k: v for k, v in sorted(team_time.items(), key=lambda item: item[1], reverse=True)}

number = 1
for equipe in team_time_sorted.keys():
    time = team_time_sorted[equipe]
    hours = int(time//60)
    mins = round(time/60%60)
    print("{}ème : {} ({}h {}min)".format(number, equipe, hours, mins))
    number += 1

print(total_time/60)
