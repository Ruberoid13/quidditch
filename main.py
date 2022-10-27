import random


def sic(t1, t2):
    rand = random.randint(0, 100)
    if rand != 100:
        print(f"{t1['score']} - {t2['score']}")
        return True
    else:
        i = random.randint(1, 2)
        if i == 1:
            t1['score'] += 150
            print(f"Snitch is catched by {t1['name']}! Match ends with:")
        else:
            t2['score'] += 150
            print(f"Snitch is catched by {t2['name']}! Match ends with:")
        print(f"{t1['name']}: {t1['score']} - {t2['name']}: {t2['score']}")
        return False


def attack(t1, t2):
    if t1['a'] == t2['d']:
        print(f"{t1['name']} attack failed")
        if t1['d'] == t2['a']:
            print(f"{t2['name']} attack failed")
        else:
            print(f"{t2['name']} attack succes")
            t2["score"] += 10
            return
    else:
        print(f"{t1['name']} attack success")
        t1["score"] += 10
        return

sl = ["Gryffindor", "Slytherin", "RavenClaw", "Hufflepuff"]
score = [0, 0]
counter = 0
t1 = {"a": 0, "d": 0, "name": sl.pop(random.randint(0, 3)), "score": 0}
t2 = {"a": 0, "d": 0, "name": sl.pop(random.randint(0, 2)), "score": 0}
print(f"Match between {t1['name']} and {t2['name']} started!")
while sic(t1, t2):
    t1['a'] = random.randint(1, 3)
    t1['d'] = random.randint(1, 3)
    t2['a'] = random.randint(1, 3)
    t2['d'] = random.randint(1, 3)
    if counter % 2 == 0:
        attack(t1, t2)
    else:
        attack(t2, t1)
    counter += 1
