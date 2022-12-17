import time

import classes

# links
leon = 'leon'
csgo = 'csgo'

# teams
team1 = 'ns'
team2 = 'ez'

# leon
coef_1_1 = 1.27
coef_1_2 = 3.5

# csgo
coef_2_1 = 1.278
coef_2_2 = 3.165

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
arb = classes.Fork(offer1, offer2, t0)
arb.get_info_profit(66)
print('\n')
