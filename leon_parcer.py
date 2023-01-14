# поиск ссылок на одинаковые ивенты
# https://leon.ru/api-2/betline/events/prematch?ctag=ru-RU&family=esport&hideClosed=true&flags=reg,mm2,rrc,nodup,urlv2
import time

import requests
import mmap
import json
import classes
from positive_parcer import get_offers_from_positive

link1 = "https://leon.ru/esports"
link2 = "https://csgopositive.me/"    #correct
link3 = "https://www.kinopoisk.ru/"
link4 = "https://leon.ru/api-2/betline/changes/inplay?ctag=ru-RU&vtag=9c2cd386-31e1-4ce9-a140-28e9b63a9300&family=esport&hideClosed=true&flags=reg,mm2,rrc,nodup,urlv2"    #correct


headers = {
  'User-agent': 'Edge 108.0.1462 (WebKit 537.36)'
}
r = requests.get(link4, headers=headers)
# with open('test.html', 'w') as output_file:
#   output_file.write(r.text.encode('cp1251'))

with open('test.html', 'w', encoding='utf-8') as output_file:
    output_file.write(r.text)
with open('test.html', 'rb', 0) as file, mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
    if s.find(b'priceStr') != -1:
        print(s.find(b'priceStr'))
        #print(s[1660])

f = open('test.html', encoding='UTF-8')
data = json.load(f)
leon_data = tuple(data.items())

# print(leon_data[4][1][0])
# event = str(leon_data[4][1][0])
# print(event[6])

# print(leon_data[4][1][0]['competitors'][0]['name'])
# print(leon_data[4][1][0]['competitors'][1]['name'])
# print(leon_data[4][1][0]['markets'][0]['runners'][0]['price'])
# print(leon_data[4][1][0]['markets'][0]['runners'][1]['price'])
# print(leon_data[4][1][10])
# print(leon_data[4][1][120]['markets'][0]['runners'][1]['priceStr'])
offers_leon = list()
for data in leon_data[3][1]:
    event_name = data['name']
    name1 = data['competitors'][0]['name']
    name2 = data['competitors'][1]['name']
    price1 = data['markets'][0]['runners'][0]['price']
    price2 = data['markets'][0]['runners'][1]['price']
    bet1 = classes.Bet('leon', name1, price1)
    bet2 = classes.Bet('leon', name2, price2)
    temp_offer = classes.Offer(bet1, bet2, event_name)
    offers_leon.append(temp_offer)

offers_positive = get_offers_from_positive()

for o_p in offers_positive:
    for o_l in offers_leon:
        if classes.compare_offers(o_p, o_l):
            fork = classes.Fork(o_p, o_l, o_p.time_of_match)
            fork.get_info_value(250)


