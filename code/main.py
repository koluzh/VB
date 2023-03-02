import random
from typing import Callable
import classes
from code.parcers.positive_parcer import get_offers_from_positive
from code.parcers.leon_parcer import get_offers_from_leon
from code.parcers.betboom_parcer import get_offers_from_betboom
from config import *
from code.parcers.olimp_parcer import get_offers_from_olimp
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 500  # Set Duration To 1000 ms == 1 second


def teams_are_equal(teams1: list[str], teams2: list[str]):
    if len(teams1) == 2 and len(teams2) == 2:
        if teams1[0] == teams2[0] and teams1[1] == teams2[1]:
            return True
        if teams1[0] == teams2[1] and teams1[1] == teams2[0]:
            return True
        return False
    else:
        Exception('wrong team names')


def get_forks(offers_1: list[classes.Offer], offers_2: list[classes.Offer]):
    forks = list()
    for o_1 in offers_1:
        for o_2 in offers_2:
            # print(o_1.bet1.team_name, o_1.bet2.team_name, o_2.bet1.team_name, o_2.bet2.team_name)
            if classes.compare_offers(o_1, o_2):
                # print('lol')
                temp_fork = classes.Fork(o_1, o_2)
                forks.append(temp_fork)
    return forks


def parse(funcs: list[Callable]):
    data_l = list()
    for f in funcs:
        # try:
        temp_l = f()
        data_l.append(temp_l)
        # except:
        #     print(f.__name__ + ' shat himself')

    forks = list()

    for i in range(len(data_l)):
        for j in range(i + 1, len(data_l)):
            forks.extend(get_forks(data_l[i], data_l[j]))
            # except:
            #     print(len(data_l))
            #     print(len(data_l[i]), len(data_l[j]))
            #     print('i think i shat myself')
            #     continue


    for f in forks:
        if f.max_profit > 0:
            print('------------------------\n')
            print('казино взломано:')
            temp = f.get_info_profit(50)
            print('------------------------\n')
            # winsound.Beep(frequency, duration)
            if temp >= 5:
                print('BIG MONEY')
                print('BIG MONEY')
                print('BIG MONEY')
                winsound.Beep(frequency, duration)
                winsound.Beep(frequency, duration)
                winsound.Beep(frequency, duration)
        else:
            print('идет взлом казино, ожидайте......')
            print(len(forks))
            print(f.offer1.bet1.team_name, f.offer1.bet2.team_name, f.offer1.link, f.offer2.link, f.max_profit)


funcs = [get_offers_from_betboom, get_offers_from_leon, get_offers_from_olimp, get_offers_from_positive]

while True:
    parse(funcs)
    time.sleep(3 * 60 + random.randint(0, 100)/100 * 60)
