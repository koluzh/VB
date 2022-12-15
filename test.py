import time

import classes

# links
leon = 'leon'
csgo = 'csgo'

# teams
team1 = 'ludus'
team2 = 'kum'

# leon
coef_1_1 = 1.45
coef_1_2 = 2.63

# csgo
coef_2_1 = 1.46
coef_2_2 = 2.52

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
arb.get_info()
