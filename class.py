import time


class Bet:
    def __init__(self, link: str, team: str, value: float, time: time.struct_time):
        self.link = link
        self.team = team
        self.value = value
        self.time = time

    def equals(self, other_bet: 'Bet'):
        if self.team == other_bet.team and self.time == other_bet.time:
            return True
        else:
            return False


class Offer:
    def __init__(self, bet1: Bet, bet2: Bet):
        self.bet1 = bet1
        self.bet2 = bet2

        if bet1.link != bet2.link or bet1.team == bet2.team:
            Exception("Invalid bets")

        self.link = bet1.link


class Arbitrage:
    def __init__(self, offer1: Offer, offer2: Offer, time: time.struct_time):
        self.time = time
        self.offer1 = offer1
        self.offer2 = offer2

        bets = [offer1.bet1, offer1.bet2, offer2.bet1, offer2.bet2]
        coef_vals = [offer1.bet1.value, offer1.bet2.value, offer2.bet1.value, offer1.bet2.value]
        hedge_val = max(coef_vals)

        for i in range(4):
            if coef_vals[i] == hedge_val:
                hedge_num = i
                break
        hedge = bets[hedge_num]

        self.hedge = hedge
        self.winner_bet = bets[(3 - hedge_num)]
        self.profitability = self.get_profit(100)

    def get_profit(self, bet_sum):
        hedge_amount = bet_sum / self.hedge.value
        winning = self.winner_bet.value * bet_sum
        return winning - hedge_amount
