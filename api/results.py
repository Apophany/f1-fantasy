import json
import urllib.request
import results_processor

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


def __write_json_to_file(path, json_file):
    with open(path, 'w') as f:
        json.dump(json_file, f)


if __name__ == "__main__":
    season = 2021
    race_num = 1

    quali_path = WRITE_PATH.format(season=season, phase='qualifying', race_num=race_num)
    race_path = WRITE_PATH.format(season=season, phase='race', race_num=race_num)
    processed_path = WRITE_PATH.format(season=season, phase='processed', race_num=race_num)

    quali_results = get_qualifying_results(season, race_num)
    race_results = get_race_results(season, race_num)
    processed_results = results_processor.process_results(quali_results, race_results)

    __write_json_to_file(quali_path, quali_results)
    __write_json_to_file(race_path, race_results)
    __write_json_to_file(processed_path, processed_results)
