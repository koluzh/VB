import time
from config import *
import winsound

class Bet:
    def __init__(self, link: str, team_name: str, value: float, time: time.struct_time = None):
        self.link = link
        self.team_name = team_name.upper().split(' ')[0]
        self.coef_value = value
        self.time_of_match = time
        self.parent = None
        self.hedge = None
        self.value = None

    def equals(self, other_bet: 'Bet'):
        if self.team_name == other_bet.team_name and self.time_of_match == other_bet.time_of_match:
            return True
        else:
            return False

    def info(self):
        print(self.team_name)
        print(self.coef_value)

class Offer:
    def __init__(self, bet1: Bet, bet2: Bet, name: str):
        self.name = name
        self.bet1 = bet1
        self.set_parent(bet1)
        self.bet2 = bet2
        self.set_parent(bet2)
        self.time_of_match = bet1.time_of_match

        if bet1.link != bet2.link or bet1.team_name == bet2.team_name or bet1.time_of_match != bet2.time_of_match:
            Exception("Invalid bets")

        self.link = bet1.link

    def set_parent(self, child: Bet):
        child.parent = self

    def info(self):
        print('\n')
        self.bet1.info()
        self.bet2.info()

class Fork:
    def __init__(self, offer1: Offer, offer2: Offer, time: time.struct_time = None):
        self.time = time
        self.offer1 = offer1
        self.offer2 = offer2
        self.bets = [offer1.bet1, offer1.bet2, offer2.bet1, offer2.bet2]
        self.max_profit = None
        self.max_profit_bet = self.get_max_profit()
        self.hedge_bet = self.max_profit_bet.hedge
        self.max_profit_bet.value = self.max_profit / self.max_profit_bet.coef_value
        self.max_value = None
        self.max_value_bet = self.get_max_value()

    def get_names(self):
        names = []
        names.append(self.offer1.bet1.team_name)
        names.append(self.offer1.bet2.team_name)
        names.append(self.offer2.bet1.team_name)
        names.append(self.offer2.bet2.team_name)
        print(names)

    def get_value(self, bet_amount: float = None, bet: Bet = None):
        if bet_amount is None:
            bet_amount = 100
        if bet is None:
            bet = self.max_value_bet

        profit = self.get_profit(bet_amount, bet)
        value = profit/bet.coef_value
        return value

    def get_max_value(self):
        max_value = self.get_value(bet=self.bets[0])
        max_value_bet = self.bets[0]

        for bet_i in self.bets:
            value = self.get_value(bet=bet_i)
            if value > max_value:
                max_value_bet = bet_i
                max_value = value

        self.max_value = max_value
        return max_value_bet

    def get_max_profit(self):
        max_profit = self.get_profit(winner=self.bets[0])
        max_profit_bet = self.bets[0]

        for bet_i in self.bets:
            profit = self.get_profit(winner=bet_i)
            if profit > max_profit:
                max_profit_bet = bet_i
                max_profit = profit

        self.max_profit = max_profit
        return max_profit_bet

    def get_profit(self, bet_amount: float = None, winner: Bet = None):
        if bet_amount is None:
            bet_amount = 100
        if winner is None:
            winner = self.max_profit_bet

        hedge = self.get_opposite_bet(winner)
        hedge_amount = bet_amount/(hedge.coef_value - 1)
        profit = winner.coef_value * bet_amount - hedge_amount - bet_amount
        return profit

    def get_opposite_bet(self, first: Bet):
        opposite_offer = self.get_opposite_offer(first.parent)

        if opposite_offer.bet1.team_name in first.team_name or first.team_name in opposite_offer.bet1.team_name:
            first.hedge = opposite_offer.bet2
            return opposite_offer.bet2
        elif opposite_offer.bet2.team_name in first.team_name or first.team_name in opposite_offer.bet2.team_name:
            first.hedge = opposite_offer.bet1
            return opposite_offer.bet1
        else:
            Exception('Invalid offers')

    def get_opposite_offer(self, first: Offer):

        if first is self.offer1:
            return self.offer2
        elif first is self.offer2:
            return self.offer1
        else:
            Exception('Invalid offers')

    def get_info_profit(self, leon_bet=None, betboom_bet=None):
        if leon_bet is None:
            leon_bet = 100
        if betboom_bet is None:
            betboom_bet = 100


        if self.max_profit_bet.link == leon:
            bet_amount = leon_bet
        if self.max_profit_bet.link == betboom:
            bet_amount = betboom_bet

        hedge_amount = bet_amount / (self.max_profit_bet.hedge.coef_value - 1)

        if self.hedge_bet.link == leon:
            if hedge_amount > leon_bet:
                hedge_amount = leon_bet
                bet_amount = hedge_amount * (self.hedge_bet.coef_value - 1)

        if self.hedge_bet.link == betboom:
            if hedge_amount > betboom_bet:
                hedge_amount = betboom_bet
                bet_amount = hedge_amount * (self.hedge_bet.coef_value - 1)

        profit = self.get_profit(bet_amount)
        loss = self.hedge_bet.coef_value * hedge_amount - bet_amount
        if loss < 0:
            print('no go')
            winsound.Beep(200, 3000)
        else:
            print('team 1: ', self.max_profit_bet.team_name, '\nsite: ', self.max_profit_bet.link, '\nbet: ', bet_amount)
            print('coef: ', self.max_profit_bet.coef_value)
            print('\nteam 2: ', self.max_profit_bet.hedge.team_name, '\nsite: ', self.max_profit_bet.hedge.link,
                  '\nbet: ', hedge_amount)
            print('coef: ', self.max_profit_bet.hedge.coef_value)
            print('\nprofit: ', profit)
            profitability = self.max_profit/(bet_amount + hedge_amount) * 100
            print('profitability: ', profitability)
            return profitability


class Query:
    def __init__(self, key: str):
        self.key = key
        self.capacity = len(key)
        self.data = list(str())
        self.size = 0

    def push_back(self, c: str):
        if len(c) != 1:
            Exception('incorrect push_back length')
            return
        if self.size < self.capacity:
            self.data.append(c)
            self.size = self.size + 1
        else:
            self.data.pop(0)
            self.data.append(c)

    def satisfied(self):
        if self.key == ''.join(self.data):
            return True
        else:
            return False

def compare_offers(offer1: Offer, offer2: Offer):
    teams1 = [offer1.bet1.team_name, offer1.bet2.team_name]
    teams2 = [offer2.bet1.team_name, offer2.bet2.team_name]
    if teams1[0] in teams2[0] and teams1[1] in teams2[1]:
        # print(teams1)
        # print(teams2)
        return True
    if teams1[0] in teams2[1] and teams1[1] in teams2[0]:
        # print(teams1)
        # print(teams2)
        return True
    return False

