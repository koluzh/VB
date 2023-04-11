import requests
from src import classes
from src.config import *
# import winsound
import json

from . import BASE_DIR


headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-length': '3581',
    'content-type': 'application/json',
    'dnt': '1',
    'origin': 'https://bifrost.oddin.gg',
    'referer': 'https://bifrost.oddin.gg/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'x-api-key': 'b94ac61d-b060-4892-8242-923bf2303a38',
    'x-display-resolution': '1115x841',
    'x-locale': 'RU',
    'x-sbi': '872d1af3-5d89-4633-9ded-a495d441d252'
}


def get_offers_from_betboom():
    # kek = get_offers_from_html('https://api-bifrost.oddin.gg/main/bifrost/query', live_events_start, end)
    req_data_path = BASE_DIR + '/req/bb_req.json'
    resp_data_path = BASE_DIR + '/data/bb_data.json'
    with open(req_data_path) as f:
        data = json.load(f)

    r = requests.post('https://api-bifrost.oddin.gg/main/bifrost/query', headers=headers, json=data)

    with open(resp_data_path, 'w', encoding=utf) as output_file:
        output_file.write(r.text)

    with open(resp_data_path, 'rb') as input_file:
        bb_data = json.load(input_file)

    bb_data = tuple(bb_data.items())

    kek = bb_data[0][1]['allMatch']['edges']

    offers = list()

    for bet_i in kek:
        try:
            node = bet_i['node']
            team1 = node['teams'][0]['team']['name']
            team2 = node['teams'][1]['team']['name']
            markets = node['mainMarketGroups'][0]['markets']
            if len(markets[0]['outcomes']) != 2:
                continue
            coef_1 = markets[0]['outcomes'][0]['odds']
            state_1 = markets[0]['outcomes'][0]['state']
            coef_2 = markets[0]['outcomes'][1]['odds']
            state_2 = markets[0]['outcomes'][1]['state']
            if state_2 != 'OPEN' or state_1 != 'OPEN':
                continue

            bet1 = classes.Bet('betboom', team1, coef_1)
            bet2 = classes.Bet('betboom', team2, coef_2)
            offer = classes.Offer(bet1, bet2, team1 + ' ' + team2)

            offers.append(offer)
        except:
            print('something went wrong, wait a little')

    return offers


if __name__ == '__main__':
    get_offers_from_betboom()
