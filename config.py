import time

# common
time_ph = time.gmtime()

leon = 'leon'
positive = 'positive'
utf = 'utf-8'

# for positive
live_events_start = 'live_enabled'
b_live_events_start = bytes(live_events_start, utf)
upcoming_events_start = 'upcoming'
b_upcoming_events_start = bytes(upcoming_events_start, utf)
event_start = 'event_cont'
b_event_start = bytes(event_start, utf)
team_name_start = 'team_name'
b_team_name_start = bytes(team_name_start, utf)
coef_start = 'sum odds_icon'
b_coef_start = bytes(coef_start, utf)
stop = '<'
b_stop = bytes(stop, utf)
event_name_start = 'event_name'
b_event_name_start = bytes(event_name_start, utf)
event_time_start = 'data-start'
b_event_time_start = bytes(event_time_start, utf)
end = 'giveaway'
b_end = bytes(end, utf)

