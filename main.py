"""
1. Добавить различные реплики комментатора
2. Оптимизировать функции
3. Прикрутить к серверу
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
            print(f"=====\nSnitch is catched by {t1['name']}!\n=====\nMatch ends with:")
        else:
            t2['score'] += 150
            print(f"=====\nSnitch is catched by {t2['name']}!\n=====\nMatch ends with:")
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

sl = ["Gryffindor", "Slytherin", "RavenClaw", "Hufflepuff"]
score = [0, 0]
counter = 0
t1 = {"a": 0, "d": 0, "name": sl.pop(random.randint(0, 3)), "score": 0}
t2 = {"a": 0, "d": 0, "name": sl.pop(random.randint(0, 2)), "score": 0}
print(f"Match between {t1['name']} and {t2['name']} started!\n")


flag = 1
print(f"{t1['name']} makes first attempt!")
while sic(t1, t2):
    t1 = rnd(t1)
    t2 = rnd(t2)
    if flag == 1:
        if attack(t1, t2) is True:
            print(f"{t1['name']} scores! Ten point for {t1['name']}!")
            t1['score'] += 10
            print(f"{t1['score']} - {t2['score']}")
            flag = 2
            print(f"{t2['name']} now attacking")
        else:
            print(f"{t2['name']} interceps the quaffle and attempting to attack!")
            flag = 2
    else:
        if attack(t2, t1) is True:
            print(f"Team {t2['name']} scores! Ten point for {t2['name']}!")
            t2['score'] += 10
            print(f"{t1['score']} - {t2['score']}")
            print(f"{t1['name']} now attacking")
            flag = 1
        else:
            print(f"Team {t1['name']} interceps the quaffle and attempting to attack!")
            flag = 1
