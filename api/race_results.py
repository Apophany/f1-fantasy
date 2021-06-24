import urllib.request
import json

RACE_RESULTS_API = "https://ergast.com/api/f1/{year}/{race_num}/results.json"
QUALIFYING_RESULTS_API = "https://ergast.com/api/f1/{year}/{race_num}/qualifying.json"
WRITE_PATH = "../data/race_results/{season}/{phase}/{race_num}.json"


def get_race_results(year: int, race_num: int):
    api_url = RACE_RESULTS_API.format(year=year, race_num=race_num)
    response = urllib.request.urlopen(api_url)
    return json.loads(__decode(response))


def get_qualifying_results(year: int, race_num: int):
    api_url = QUALIFYING_RESULTS_API.format(year=year, race_num=race_num)
    response = urllib.request.urlopen(api_url)
    return json.loads(__decode(response))


def __decode(url_response):
    return url_response.read().decode(url_response.info().get_param('charset') or 'utf-8')


if __name__ == "__main__":
    season = 2021
    race_num = 1

    quali_path = WRITE_PATH.format(season=season, phase='qualifying', race_num=race_num)
    race_path = WRITE_PATH.format(season=season, phase='race', race_num=race_num)

    with open(quali_path, 'w') as f:
        json.dump(get_qualifying_results(season, race_num), f)

    with open(race_path, 'w') as f:
        json.dump(get_race_results(season, race_num), f)
