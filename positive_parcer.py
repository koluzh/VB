import requests
import mmap
import classes
import time
import datetime as dt
from config import *
import random
import winsound

link4 = "https://csgopositive.me/"    #correct


headers = {
  'User-agent': 'Edge 108.0.1462 (WebKit 537.36)'
}


def get_offers_from_positive():
    r = requests.get(link4, headers=headers)
    with open('temp.html', 'w', encoding=utf) as output_file:
        output_file.write(r.text)

    with open('temp.html', 'rb', 0) as file, mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as b_f:
        end = b_f.find(b_end)
        b_f.seek(0)
        start = b_f.find(b_live_events_start)
        try:
            b_f.seek(start)
        except:
            print('sleeping')
            #winsound.Beep(1000, 500)
            time.sleep(random.randint(10, 20))
            #winsound.Beep(2000, 500)
        stop = b_f.find(bytes(upcoming_events_start, utf))

        offers = list()

        while b_f.tell() != end and b_f.tell() < stop:
            temp_offer = get_offer(b_f, end)
            if b_f.tell() > stop:
                break
            if temp_offer is None:
                return offers
            offers.append(temp_offer)
        return offers

def get_offer(f_map: mmap.mmap, end: int):
    start = f_map.find(b_event_start)
    if start >= end:
        return None
    f_map.seek(start)
    bet1 = get_bet(f_map)
    event = get_event(f_map)
    bet2 = get_bet(f_map)
    bet1.time_of_match = event['event_time']
    bet2.time_of_match = event['event_time']
    offer = classes.Offer(bet1, bet2, event['event_name'])
    return offer


def get_str(f_map: mmap.mmap):
    f_map.seek(-1, 1)
    start = f_map.find(bytes('>', utf))
    f_map.seek(start + 1)
    string = list()
    while f_map.tell() != f_map.size():
        b_char = f_map.read(1)
        if b_char == b_stop:
            break
        try:
            char = b_char.decode(utf)
        except:
            continue
        string.append(char)
    string = ''.join(string)
    return string

def get_bet(f_map: mmap.mmap):
    team_name_pos = f_map.find(b_team_name_start)
    f_map.seek(team_name_pos)
    team_name = get_str(f_map)
    coef_pos = f_map.find(b_coef_start)
    f_map.seek(coef_pos)
    coef = float(get_str(f_map))
    bet = classes.Bet(positive, team_name, coef)
    return bet

def str_to_time(time_str: str):
    month = time_str[:2]
    month = int(month)
    time_str = time_str[3:]
    day = time_str[:2]
    day = int(day)
    time_str = time_str[3:]
    year = time_str[:4]
    year = int(year)
    time_str = time_str[5:]
    hour = time_str[:2]
    hour = int(hour)
    time_str = time_str[3:]
    minutes = time_str[:2]
    minutes = int(minutes)
    time_str = time_str[3:]
    seconds = time_str[:2]
    seconds = int(seconds)
    event_time = dt.datetime(year, month, day, hour, minutes, seconds).timetuple()
    event_time = time.struct_time(event_time)
    return event_time


def get_event_time(f_map: mmap.mmap):
    while f_map.tell() != f_map.size():
        b_char = f_map.read(1)
        char = b_char.decode(utf)
        if char == '\"':
            break
    ans = list()
    while f_map.tell() != f_map.size():
        b_char = f_map.read(1)
        char = b_char.decode(utf)
        if char != '\"':
            ans.append(char)
        else:
            break
    ans = ''.join(ans)
    return ans



def get_event(f_map: mmap.mmap):
    event_name_start = f_map.find(b_event_name_start)
    f_map.seek(event_name_start)
    event_name = get_str(f_map)
    event_time_start = f_map.find(b_event_time_start)
    f_map.seek(event_time_start)
    event_time = get_event_time(f_map)
    event = {
        'event_name': event_name,
        'event_time': event_time
    }
    return event


if __name__ == '__main__':
    kek = get_offers_from_positive()
    for lol in kek:
        print(lol.bet1.__dict__)
        print(lol.bet2.__dict__)
        print('\n')

