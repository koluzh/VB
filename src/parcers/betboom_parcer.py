import requests
import src.parcers.classes as classes
import json


headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-length': '3581',
    'content-type': 'application/json',
    'dnt': '1',
    'origin': 'https://bifrost.oddin.gg',
    'referer': 'https://bifrost.oddin.gg/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'x-api-key': 'b94ac61d-b060-4892-8242-923bf2303a38',
    'x-display-resolution': '1115x841',
    'x-locale': 'RU',
    'x-sbi': '872d1af3-5d89-4633-9ded-a495d441d252'
}


def get_offers_from_betboom():
    # kek = get_offers_from_html('https://api-bifrost.oddin.gg/main/bifrost/query', live_events_start, end)
    req_data = {
        "operationName": "allMatch",
        "variables":
        {
            "first": 20,
            "liveOnly": False,
            "historic": False,
            "favourites": None,
        },
        "query": "query allMatch($after: String, $before: String, $first: Int, $last: Int, $liveOnly: Boolean, "
                 "$sports: [ID!], $tournaments: [ID!], $historic: Boolean, $favourites: Boolean, $search: String) {\n "
                 " allMatch(\n    after: $after\n    before: $before\n    first: $first\n    last: $last\n    "
                 "liveOnly: $liveOnly\n    sports: $sports\n    tournaments: $tournaments\n    historic: $historic\n  "
                 "  favourites: $favourites\n    text: $search\n  ) {\n    edges {\n      node {\n        id\n        "
                 "marketsCount\n        stream {\n          url\n          streamProvider\n          __typename\n     "
                 "   }\n        favourite\n        ...MatchBase\n        ...MatchMainMarketGroups\n        "
                 "...MatchPeriods\n        ...MatchScoreboard\n        __typename\n      }\n      __typename\n    }\n "
                 "   pageInfo {\n      hasNextPage\n      hasPreviousPage\n      startCursor\n      endCursor\n      "
                 "__typename\n    }\n    total\n    __typename\n  }\n}\n\nfragment MatchBase on Match {\n  "
                 "datePlannedStart\n  state\n  prematchOnly\n  ...MatchTeams\n  ...MatchTournament\n  "
                 "__typename\n}\n\nfragment MatchTeams on Match {\n  teams {\n    team {\n      id\n      name\n      "
                 "icon\n      __typename\n    }\n    winner\n    __typename\n  }\n  __typename\n}\n\nfragment "
                 "MatchTournament on Match {\n  tournament {\n    id\n    name\n    favourite\n    sport {\n      "
                 "id\n      icon\n      name\n      __typename\n    }\n    __typename\n  }\n  "
                 "__typename\n}\n\nfragment MatchMainMarketGroups on Match {\n  mainMarketGroups {\n    id\n    "
                 "name\n    namePrefix\n    layoutType\n    independenceId\n    selections {\n      id\n      name\n  "
                 "    __typename\n    }\n    markets {\n      id\n      info\n      state\n      outcomes {\n        "
                 "id\n        odds\n        state\n        won\n        __typename\n      }\n      __typename\n    "
                 "}\n    __typename\n  }\n  __typename\n}\n\nfragment MatchPeriods on Match {\n  periods {\n    "
                 "number\n    homeScore\n    awayScore\n    periodScore {\n      ... on KillsPeriodScore {\n        "
                 "homeKills\n        awayKills\n        __typename\n      }\n      ... on RoundsPeriodScore {\n       "
                 " homeWonRounds\n        awayWonRounds\n        __typename\n      }\n      ... on GoalsPeriodScore {"
                 "\n        homeGoals\n        awayGoals\n        __typename\n      }\n      __typename\n    }\n    "
                 "__typename\n  }\n  activePeriod\n  __typename\n}\n\nfragment MatchScoreboard on Match {\n  "
                 "scoreboard {\n    ... on CsgoScoreboard {\n      homeCtTeam\n      homeWonRounds\n      "
                 "awayWonRounds\n      currentRound\n      __typename\n    }\n    ... on CsgoWingmanScoreboard {\n    "
                 "  homeCtTeam\n      homeWonRounds\n      awayWonRounds\n      currentRound\n      __typename\n    "
                 "}\n    ... on LolScoreboard {\n      homeKills\n      awayKills\n      homeDestroyedTurrets\n      "
                 "awayDestroyedTurrets\n      homeGold\n      awayGold\n      __typename\n    }\n    ... on "
                 "Dota2Scoreboard {\n      homeKills\n      awayKills\n      homeDestroyedTowers\n      "
                 "awayDestroyedTowers\n      homeGold\n      awayGold\n      __typename\n    }\n    ... on "
                 "KogScoreboard {\n      homeKills\n      awayKills\n      homeDestroyedTurrets\n      "
                 "awayDestroyedTurrets\n      homeGold\n      awayGold\n      __typename\n    }\n    ... on "
                 "RSoccerScoreboard {\n      homeGoals\n      awayGoals\n      __typename\n    }\n    ... on "
                 "ValorantScoreboard {\n      homeDefenderTeam\n      homeWonRounds\n      awayWonRounds\n      "
                 "currentRound\n      __typename\n    }\n    __typename\n  }\n  __typename\n} "
    }
    r = requests.post('https://api-bifrost.oddin.gg/main/bifrost/query', headers=headers, json=req_data)

    if r.status_code == 429:
        raise classes.TimeOut()

    bb_data = json.loads(r.text)
    # print(bb_data)

    kek = bb_data['data']['allMatch']['edges']

    if len(kek) == 0:
        raise classes.NoMarkets()

    offers = list()

    for bet_i in kek:
        try:
            node = bet_i['node']
            team1 = node['teams'][0]['team']['name']
            team2 = node['teams'][1]['team']['name']
            markets = node['mainMarketGroups'][0]['markets']
            if len(markets[0]['outcomes']) != 2:
                continue
            coef_1 = markets[0]['outcomes'][0]['odds']
            state_1 = markets[0]['outcomes'][0]['state']
            coef_2 = markets[0]['outcomes'][1]['odds']
            state_2 = markets[0]['outcomes'][1]['state']
            if state_2 != 'OPEN' or state_1 != 'OPEN':
                continue

            bet1 = classes.Bet('betboom', team1, coef_1)
            bet2 = classes.Bet('betboom', team2, coef_2)
            offer = classes.Offer(bet1, bet2, team1 + ' ' + team2)

            offers.append(offer)
        except Exception as e:
            print(e)
            continue

    return offers


if __name__ == '__main__':
    offers = get_offers_from_betboom()
    for o in offers:
        print(o.info())
