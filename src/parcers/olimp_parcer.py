import requests
import json

import src.parcers.classes as classes
from src.parcers import *

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}


def get_offers_from_olimp():
    r = requests.get('https://www.olimp.bet/api/v4/0/live/sports-with-competitions-with-events', headers=headers)

    if __name__ == '__main__':
        print(r.status_code)

    data_dir = BASE_DIR + '/data/ob_data.json'

    with open(data_dir, 'w', encoding=utf) as output_file:
        output_file.write(r.text)

    with open(data_dir, 'rb') as input_file:
        ob_data = json.load(input_file)

    ob_data = ob_data[5]
    ob_data = dict(ob_data.items())

    comps = ob_data['payload']['competitionsWithEvents']

    offers = list()

    for c in comps:
        try:
            events = c['events']
            for e in events:
                name = e['name']
                team_1 = e['team1Name']
                team_2 = e['team2Name']

                oc = e['outcomes']

                coef_1 = float(oc[0]['probability'])
                coef_2 = float(oc[1]['probability'])

                bet_1 = classes.Bet(olimp, team_1, coef_1)
                bet_2 = classes.Bet(olimp, team_2, coef_2)

                offer = classes.Offer(bet_1, bet_2, name)
                offers.append(offer)
        except:
            continue

    return offers


if __name__ == '__main__':
    offers = get_offers_from_olimp()
    for o in offers:
        print(o.info())
