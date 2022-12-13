class Bet:
    def __init__(self, coef1, coef2):
        self.coef1 = coef1
        self.coef2 = coef2


class Arbitrage:
    def __init__(self, bet1: Bet, bet2: Bet):
        self.bet1 = bet1
        self.bet2 = bet2
