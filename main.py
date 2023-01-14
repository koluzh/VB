from classes import Offer
from positive_parcer import get_offers_from_positive
# from leon_parcer import get_offers_from_positive
from config import *


def teams_are_equal(teams1: list[str], teams2: list[str]):
    if len(teams1) == 2 and len(teams2) == 2:
        if teams1[0] == teams2[0] and teams1[1] == teams2[1]:
            return True
        if teams1[0] == teams2[1] and teams1[1] == teams2[0]:
            return True
        return False
    else:
        Exception('wrong team names')





offers_from_positive = get_offers_from_positive()
for i in offers_from_positive:
    print(i.bet1.team_name)
    print(i.bet2.team_name)
offers_from_leon = list()

