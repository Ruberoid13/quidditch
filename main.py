"""
1. Добавить различные реплики комментатора
2. Оптимизировать функции
3. Прикрутить к серверу
4. Добавить комментарии к направлениям атаки и успешной защиты


1.Матч между командами {team_names[t1['name']][1]} и {team_names[t2['name']][1]} начался!
Матч Слизерин - Когтевран начался!
Слизерин и Когтевран сошлись на поле! Пусть победит сильнейший!

2.Игроки {team_names[t1['name']][1]} выигрывают вбрасывание и устремляются к воротам соперника!
Вбрасывание за Когтевраном, Слизерин обороняется.
Вбрасывание, и квоффл оказзывается в руках охотников из Когтеврана!

3.Команда {team_names[t1['name']][1]} забрасывает мяч в ворота соперника!
Команда Пуффендуя не смогла остановить натиск Гриффиндора и теперь будет отыгрываться!
Командная работа принесла плоды - квоффл пролетает сквозь ворота соперников Гриффиндора!
Охотник из Гриффиндора оказался ловчее вратаря Пуффендуя!

4.Десять очков {team_names[t1['name']][2]}!


5.{team_names[t2['name']][0]} атакует
Пуффендуй рвется к воротам соперника
Слизерин пытается остановить натиск Пуффендуя
Пуффендуй в атаке

6.Команда {team_names[t2['name']][1]} перехватывает квоффл и устремляется в атаку!
Квоффл перехвачен, и теперь Гриффиндор атакует!
Игроки Слизерина не смогли удержать квоффл, и теперь обороняются!
Охотник Слизерина теряет квоффл, команда Гриффиндора мчится к воротам соперника!

7.Снитч пойман {team_names[t1['name']][4]}!
Ловец Слизерина поймал снитч!
Снитч попался в руки ловца Слизерина!

8.Матч окончен со счетом:
Матч завершен, итоговый счет:
Бойня окончена, потерь почти нет.
"""
import random


def sic(t1, t2):
    rand = random.randint(0, 100)
    if rand != 100:
        return True
    else:
        i = random.randint(1, 2)
        if i == 1:
            t1['score'] += 150
            print(f"=====\nСнитч пойман {team_names[t1['name']][4]}!\n=====\n"
                  f"Матч окончен со счетом:")
            # print(f"=====\nSnitch is catched by {t1['name']}!\n=====\nMatch ends with:")
        else:
            t2['score'] += 150
            print(f"=====\nСнитч пойман {team_names[t2['name']][4]}!\n=====\n"
                  f"Матч окончен со счетом:")
        print(f"{t1['name']}: {t1['score']} - {t2['name']}: {t2['score']}")
        return False


def attack(t1, t2):
    if t1['a'] == t2['d']:
        return True
    else:
        return False


def rnd(team):
    team['a'] = random.randint(1, 3)
    team['d'] = random.randint(1, 3)
    return team


def rnd_announce(in_list):
    print(f"{in_list[random.randint(0, len(in_list) - 1)]}\n")


# sl = ["Gryffindor", "Slytherin", "RavenClaw", "Hufflepuff"]
sl = ["Гриффиндор", "Слизерин", "Когтевран", "Пуффендуй"]
team_names = {"Гриффиндор": ["Гриффиндор", "Гриффиндора", "Гриффиндору", "Гриффиндор", "Гриффиндором", "Гриффиндоре"],
"Слизерин": ["Слизерин", "Слизерина", "Слизерину", "Слизерин", "Слизерином", "Слезерене"],
"Когтевран": ["Когтевран", "Когтеврана", "Когтеврану", "Когтевран", "Когтевраном", "Когтевране"],
"Пуффендуй": ["Пуффендуй", "Пуффендуя", "Пуффендую", "Пуффендуй", "Пуффендуем", "Пуффендуе"],
}
# score = [0, 0]
# counter = 0
t1 = {"a": 0, "d": 0, "name": sl.pop(random.randint(0, 3)), "score": 0}
t2 = {"a": 0, "d": 0, "name": sl.pop(random.randint(0, 2)), "score": 0}
flag = 1

match_started = [f"Матч между командами {team_names[t1['name']][1]} и {team_names[t2['name']][1]} начался!",
                 f"Матч {team_names[t1['name']][0]} - {team_names[t2['name']][0]} начался!",
                 f"{team_names[t1['name']][0]} и {team_names[t2['name']][0]} сошлись на поле! Пусть победит сильнейший!"]
throw_in = []
goal = []
ten_points = []
attack_ = []
intercept = []
sic_ = []
match_ended = []

# speech = {"match_started":[],
#           "throw-in": [],
#           "goal": [],
#           "ten_points": [],
#           "attack": [],
#           "intercept": [],
#           "sic": [],
#           "match_ended": []}

rnd_announce(match_started)
# print(f"Матч между командами {team_names[t1['name']][1]} и {team_names[t2['name']][1]} начался!\n")
print(f"Игроки {team_names[t1['name']][1]} выигрывают розыгрыш и устремляются к воротам соперника!")
while sic(t1, t2):
    t1 = rnd(t1)
    t2 = rnd(t2)
    if flag == 1:
        if attack(t1, t2) is True:
            print(f"Команда {team_names[t1['name']][1]} забрасывает мяч в вороота соперника!"
                  f" Десять очков {team_names[t1['name']][2]}!")
            t1['score'] += 10
            print(f"{t1['score']} - {t2['score']}")
            print(f"{team_names[t2['name']][0]} атакует")
            flag = 2
        else:
            print(f"Команда {team_names[t2['name']][1]} перехватывает квоффл и устремляется в атаку!")
            flag = 2
    else:
        if attack(t2, t1) is True:
            print(f"Команда {team_names[t2['name']][1]} забрасывает мяч в вороота соперника!"
                  f" Десять очков {team_names[t1['name']][2]}!")
            t2['score'] += 10
            print(f"{t1['score']} - {t2['score']}")
            print(f"{team_names[t1['name']][0]} атакует")
            flag = 1
        else:
            print(f"Команда {team_names[t1['name']][1]} перехватывает квоффл и устремляется в атаку!")
            flag = 1
