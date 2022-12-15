import time

class Bet:
    def __init__(self, link: str, team_name: str, value: float, time: time.struct_time):
        self.link = link
        self.team_name = team_name
        self.coef_value = value
        self.time_of_match = time
        self.parent = None
        self.hedge = None

    def equals(self, other_bet: 'Bet'):
        if self.team_name == other_bet.team_name and self.time_of_match == other_bet.time_of_match:
            return True
        else:
            return False


class Offer:
    def __init__(self, bet1: Bet, bet2: Bet):
        self.bet1 = bet1
        self.set_parent(bet1)
        self.bet2 = bet2
        self.set_parent(bet2)

        if bet1.link != bet2.link or bet1.team_name == bet2.team_name:
            Exception("Invalid bets")

        self.link = bet1.link

    def set_parent(self, child: Bet):
        child.parent = self


class Arbitrage:
    def __init__(self, offer1: Offer, offer2: Offer, time: time.struct_time):
        self.time = time
        self.offer1 = offer1
        self.offer2 = offer2
        self.bets = [offer1.bet1, offer1.bet2, offer2.bet1, offer2.bet2]
        self.max_profit = None
        self.max_profit_bet = self.get_max_profit()

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
        hedge_amount = bet_amount/hedge.coef_value
        profit = winner.coef_value * bet_amount - hedge_amount - bet_amount
        return profit

    def get_opposite_bet(self, first: Bet):
        opposite_offer = self.get_opposite_offer(first.parent)

        if opposite_offer.bet1.equals(first):
            first.hedge = opposite_offer.bet2
            return opposite_offer.bet2
        elif opposite_offer.bet2.equals(first):
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
