import requests
import json

from src.parcers import classes
from src.parcers import *

link4 = "https://leon.ru/api-2/betline/events/prematch?ctag=ru-RU&family=esport&hideClosed=true&flags=reg,urlv2,mm2,rrc,nodup"    #correct


headers = {
  'User-agent': 'Edge 108.0.1462 (WebKit 537.36)'
}


def get_offers_from_leon():
    r = requests.get(link4, headers=headers)
    if r.status_code == 429:
        raise classes.TimeOut('OBTO')

    if __name__ == '__main__':
        print('request status code:', r.status_code)

    leon_data = json.loads(r.text)

    # if not leon_data.get('enabled'):
    #     raise classes.NoMarkets()

    if __name__ == '__main__':
        print(leon_data)
        data_dir = BASE_DIR + '/data/leon_data.json'
        with open(data_dir, 'w', encoding='utf-8') as output_file:
            output_file.write(r.text)

    # print(data)

    offers_leon = list()

    for data in leon_data["events"]:
        try:
                event_name = data['name']
                name1 = data['competitors'][0]['name']
                name2 = data['competitors'][1]['name']
                hw1_1 = data['competitors'][0]['homeAway']
                hw1_2 = data['competitors'][1]['homeAway']

                if data['markets'][0]['name'] != 'Победитель':  # ?
                    if __name__ == "__main__":
                        print(name1, name2, 'kekekek')
                    continue
                runners = data['markets'][0]['runners']
                # price1 = data['markets'][0]['runners'][0]['price']
                # price2 = data['markets'][0]['runners'][2]['price']
                price = dict()
                for r in runners:
                    price[r['name']] = r['price']

                hw2_1 = data['markets'][0]['runners'][0]['tags'][0]
                hw2_2 = data['markets'][0]['runners'][1]['tags'][0]

                state_1 = data['markets'][0]['runners'][0]['open']
                state_2 = data['markets'][0]['runners'][1]['open']

                if state_2 is False or state_1 is False:
                    continue

                hw = [hw1_1, hw1_2, hw2_1, hw2_2]
                # print(data, '\n', hw)
                if hw1_1 != hw2_1:
                    name1, name2 = name2, name1
                bet1 = classes.Bet('leon', name1, price['1'])
                bet2 = classes.Bet('leon', name2, price['2'])
                temp_offer = classes.Offer(bet1, bet2, event_name)
                offers_leon.append(temp_offer)
        except Exception as e:
            continue

    return offers_leon


if __name__ == '__main__':
    offers = get_offers_from_leon()
    if type(offers) == Exception:
        print(offers)
    else:
        for o in offers:
            print(o.info())
    print(len(offers))




