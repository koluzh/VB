# поиск ссылок на одинаковые ивенты
#https://leon.ru/api-2/betline/events/prematch?ctag=ru-RU&family=esport&hideClosed=true&flags=reg,mm2,rrc,nodup,urlv2
import requests
import mmap
import classes
import json
from html.parser import HTMLParser


class MyParser(HTMLParser):
    pass


link1 = "https://leon.ru/esports"
link2 = "https://csgopositive.me/"    #correct
link3 = "https://www.kinopoisk.ru/"
link4 = "https://csgopositive.me/"    #correct


headers = {
  'User-agent': 'Edge 108.0.1462 (WebKit 537.36)'
}
r = requests.get(link4, headers=headers)
with open('test.html', 'w', encoding='utf-8') as output_file:
    output_file.write(r.text)
with open('test.html', 'rb', 0) as file, mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
    start = s.find(b'event_cont')
    end = s.rfind(b'event_cont')
print(start, end)

kek = MyParser()