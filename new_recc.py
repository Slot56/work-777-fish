import requests
from pprint import pprint
import json

# url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"

response = requests.get(url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json")
print("Смотрим ответ сервера:", response.status_code)
print(type(response.json()))
hero_list = json.dumps(response.json())
and_1 = json.loads(hero_list)
# pprint(type(and_1))

# умный(intelligence) из трех супергероев- Hulk, Captain America, Thanos.
hero_l_1 = ["Hulk", "Captain America", "Thanos" ]

hero_l_2 = []

for and_2 in and_1:
    if and_2["name"] == "Hulk":
        hulks  = and_2["powerstats"]["intelligence"]
        if hulks < 150:
            hero_l_2.append(hulks)
        # print(hulks)

for and_2 in and_1:
    if and_2["name"] == "Captain America":
        captains  = and_2["powerstats"]["intelligence"]
        if captains < 150:
            hero_l_2.append(captains)
        # pprint(captains)

for and_2 in and_1:
    if and_2["name"] == "Thanos":
        thanoss = and_2["powerstats"]["intelligence"]
        if thanoss < 150:
            hero_l_2.append(thanoss)
        # pprint(thanoss)

# pprint(type(hulks))

pprint(hero_l_2)

hero_3 = dict(zip(hero_l_1, hero_l_2))
pprint(hero_3)

# for hero in hero_3.values():
    # pprint(hero)
    # pprint(type(hero))

intelligence_max = (max(hero_3))
pprint("Самый умный герой - это: {}".format(intelligence_max))