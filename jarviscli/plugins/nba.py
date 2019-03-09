from plugin import plugin
from basketball_reference_web_scraper import client
import datetime
@plugin("nba")
def nbascores(jarvis, s):
    d = datetime.now()
    pyyear = int(d.strftime('%Y'))
    pymonth = int(d.strftime('%m'))
    pyday= int(d.strftime('%d'))
    s = client.team_box_scores(day=pyday, month=pymonth, year=pyyear)
    jarvis.say(s)
