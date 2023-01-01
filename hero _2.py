# Импортируем библиотеку requests для получения данных страницы, на которой размещен json файл. Распаковываем его с помощью json. В полученном словаре в "results" в "powerstats" есть параметр "intelligence", в котором и хранится нужная информация:
import requests
import json

heroes_list = ['Hulk', 'Captain america', 'Thanos']
#создадим словарь, в котором будет находиться информация о интеллекте каждого героя (изначально 0)
intelligence_dict = {'Hulk': 0, 'Captain america': 0, 'Thanos': 0}
url = 'https://akabab.github.io/superhero-api/api/powerstats/1.json'
url = requests.get("https://akabab.github.io/superhero-api/api/powerstats/1.json")
print(url.status_code)

for hero in heroes_list:
    hero_dict = json.loads(requests.get(url + hero).content)
    intelligence_dict[hero] = int(hero_dict['results'][0]['powerstats']['intelligence'])
    