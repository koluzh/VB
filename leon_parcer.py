# поиск ссылок на одинаковые ивенты
# https://leon.ru/api-2/betline/events/prematch?ctag=ru-RU&family=esport&hideClosed=true&flags=reg,mm2,rrc,nodup,urlv2
import requests
import mmap
import json
import classes

link1 = "https://leon.ru/esports"
link2 = "https://csgopositive.me/"    #correct
link3 = "https://www.kinopoisk.ru/"
link4 = "https://leon.ru/api-2/betline/events/prematch?ctag=ru-RU&family=esport&hideClosed=true&flags=reg,mm2,rrc,nodup,urlv2"    #correct


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
for number in range(len(leon_data[4][1])-1):
    print(number)
    try:
        print('team1:  ', leon_data[4][1][number]['competitors'][0]['name'])
        print('team2:  ', leon_data[4][1][number]['competitors'][1]['name'])
        print('coef1:  ', leon_data[4][1][number]['markets'][0]['runners'][0]['price'])
        print('coef2:  ', leon_data[4][1][number]['markets'][0]['runners'][1]['price'])
    except IndexError:
        print('index error\n\n\n')




