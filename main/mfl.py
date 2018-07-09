import requests
from django.conf import settings


class MFL:
    def __init__(self):
        self.username = 'croozer'
        self.password = settings.MFL_PASS
        self.league = 74575
        self.url = 'https://www62.myfantasyleague.com/2018/login?USERNAME={}&PASSWORD={}'.format(self.username, self.password)
        self.api_key = 'bRdp18CSvuKnx1GmP13EZjceEKctiQ'
        self.json = 1
        self.params = {'USERNAME': self.username, 'PASSWORD': self.password, 'APIKEY': self.api_key, 'JSON': self.json, 'L': self.league}
        self.export_url = 'http://www62.myfantasyleague.com/2018/export?{}'.format(self.params)


    def export(self, params):
        merged_params = {params, self.params}
        return requests.get(self)


    def login(self):

        params = {'TYPE': 'login'}
        result = requests.get(self.url, params=params)

        return result

    def rosters(self, id = None):
        params = {'TYPE': 'rosters'}
        url = 'http://www62.myfantasyleague.com/2018/export?TYPE=rosters&L=74575&APIKEY=bRdp18CSvuKnx1GmP13EZjceEKctiQ%3D%3D&FRANCHISE={}&JSON=1'.format(id)
        result = requests.get(url)
        return result

    def get_league(self):
        params = {'TYPE': 'league'}
        url = 'http://www62.myfantasyleague.com/2018/export?TYPE=league&L=74575&APIKEY=bRdp18CSvuKnx1GmP13EZjceEKctiQ%3D%3D&FRANCHISE=&JSON=1'
        result = requests.get(url).text
        return result

