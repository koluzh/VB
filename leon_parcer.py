import requests
import mmap
import json
import classes

link4 = "https://leon.ru/api-2/betline/changes/inplay?ctag=ru-RU&vtag=9c2cd386-31e1-4ce9-a140-28e9b63a9300&family=esport&hideClosed=true&flags=reg,mm2,rrc,nodup,urlv2"    #correct


headers = {
  'User-agent': 'Edge 108.0.1462 (WebKit 537.36)'
}
def get_offers_from_leon():
    r = requests.get(link4, headers=headers)

    with open('kek.json', 'w', encoding='utf-8') as output_file:
        output_file.write(r.text)
    with open('kek.json', 'rb', 0) as file, mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
        if s.find(b'priceStr') != -1:
            pass
            #print(s.find(b'priceStr'))
            #print(s[1660])

    f = open('kek.json', encoding='UTF-8')
    data = json.load(f)
    leon_data = tuple(data.items())
    #print(data)

    offers_leon = list()

    for data in leon_data[3][1]:
        try:
            event_name = data['name']
            name1 = data['competitors'][0]['name']
            name2 = data['competitors'][1]['name']
            hw1_1 = data['competitors'][0]['homeAway']
            hw1_2 = data['competitors'][1]['homeAway']

            price1 = data['markets'][0]['runners'][0]['price']
            price2 = data['markets'][0]['runners'][1]['price']
            hw2_1 = data['markets'][0]['runners'][0]['tags'][0]
            hw2_2 = data['markets'][0]['runners'][1]['tags'][0]
            hw = [hw1_1, hw1_2, hw2_1, hw2_2]
            # print(data, '\n', hw)
            if hw1_1 != hw2_1:
                name1, name2 = name2, name1
            bet1 = classes.Bet('leon', name1, price1)
            bet2 = classes.Bet('leon', name2, price2)
            temp_offer = classes.Offer(bet1, bet2, event_name)
            offers_leon.append(temp_offer)
        except:
            print('no markets')

    return offers_leon




