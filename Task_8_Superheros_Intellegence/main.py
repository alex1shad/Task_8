import requests


def sups_intel():
    heroes = {'Hulk': '',
              'Captain America': '',
              'Thanos': ''}
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    resp = requests.get(url).json()
    for el in resp:
        if el['name'] in heroes.keys():
            heroes[el['name']] = el['powerstats']['intelligence']
    print(sorted(zip(heroes.values(), heroes.keys()))[-1][1])


if __name__ == '__main__':
    sups_intel()
