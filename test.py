import time

import classes

# links
leon = 'leon'
csgo = 'csgo'

# teams
team1 = 'cu'
team2 = 'ns'

# leon
coef_1_1 = 2.86
coef_1_2 = 1.38

# csgo
coef_2_1 = 3.003
coef_2_2 = 1.308

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
arb.get_info_profit()
print('\n')
arb.get_info_value()
