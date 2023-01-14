import time

import classes

# links
leon = 'leon'
csgo = 'csgo'

# teams
team1 = 'dvorak'
team2 = 'kape'

# leon
coef_1_1 = 3.69
coef_1_2 = 1.27

# csgo
coef_2_1 = 3.253
coef_2_2 = 1.263

# get_time
t0 = time.time()
t0 = time.gmtime(t0)

# objects
bet1 = classes.Bet(leon, team1, coef_1_1, t0)
bet2 = classes.Bet(leon, team2, coef_1_2, t0)
bet3 = classes.Bet(csgo, team1, coef_2_1, t0)
bet4 = classes.Bet(csgo, team2, coef_2_2, t0)

# offers
offer1 = classes.Offer(bet1, bet2, "kek")
offer2 = classes.Offer(bet3, bet4, "lol")

# arbitrage
arb = classes.Fork(offer1, offer2, t0)
arb.get_info_profit(100)
print('\n')
