import random

import classes
from positive_parcer import get_offers_from_positive
from leon_parcer import get_offers_from_leon
from betboom_parcer import get_offers_from_betboom
from config import *
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


def get_offers(max_time: int = None):
    while True:
        offers_positive = get_offers_from_positive()
        offers_leon = get_offers_from_leon()
        offers_betboom = get_offers_from_betboom()
        start = time.time()
        k = 0
        for o_p in offers_betboom:
            for o_l in offers_leon:
                # print((o_p.bet1.team_name, o_p.bet2.team_name, o_l.bet1.team_name, o_l.bet2.team_name))
                if classes.compare_offers(o_p, o_l):
                    k = k + 1
                    fork = classes.Fork(o_p, o_l, o_p.time_of_match)
                    if fork.max_profit > 0:
                        print('------------------------\n')
                        print('казино взломано:')
                        temp = fork.get_info_profit(leon_bet=150, betboom_bet=150)
                        print('------------------------\n')
                        if temp > 10:
                            print('BIG MONEY')
                            print('BIG MONEY')
                            print('BIG MONEY')
                            winsound.Beep(frequency, duration)
                            winsound.Beep(frequency, duration)
                    else:
                        print('идет взлом казино......')
        print('betboom: ', len(offers_betboom))
        print('leon: ', len(offers_leon))
        print('совпадения: ', k)
        time.sleep(5 + random.randint(0, 15) / 10)
        if max_time is not None:
            if time.time() - start > max_time:
                break


get_offers()

