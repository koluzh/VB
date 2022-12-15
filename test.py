import time

import classes

# links
leon = 'csgopositive'
csgo = 'leon'

# teams
team1 = 'ftw'
team2 = 'forze'

# leon
coef_1_1 = 2.31
coef_1_2 = 1.57

# csgo
coef_2_1 = 2.041
coef_2_2 = 1.68

# get_time
t0 = time.time()
t0 = time.gmtime(t0)

# objects
bet1 = classes.Bet(leon, team1, coef_1_1, t0)
bet2 = classes.Bet(leon, team2, coef_1_2, t0)
bet3 = classes.Bet(csgo, team1, coef_2_1, t0)
bet4 = classes.Bet(csgo, team2, coef_2_2, t0)

# offers
offer1 = classes.Offer(bet1, bet2)
offer2 = classes.Offer(bet3, bet4)

# arbitrage
arb = classes.Arbitrage(offer1, offer2, t0)
money = arb.get_profit(200)
print(money)
print(arb.max_profit_bet.coef_value)
print(arb.max_profit_bet.hedge.coef_value)
