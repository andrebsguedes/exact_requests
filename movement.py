import requests
import login
from lxml import html


class Movement:
    def __init__(self, sender, target, type, troops):
        self.sender = sender
        self.target = target
        self.type = type
        self.troops = troops
        self.action_id = None
        self.ch = None

    def update_data(self, session):
        if not login.is_logged_in(session):
            return False
        data = self.get_post_data()
        url = 'http://br62.tribalwars.com.br/game.php?village=' + \
            self.sender+'&try=confirm&screen=place'
        r = requests.post(url, data=data, cookies=session)
        action_page = html.fromstring(r.text)
        if(len(action_page.xpath('//input[@name="action_id"]/@value')) != 0):
            self.action_id = \
                action_page.xpath('//input[@name="action_id"]/@value')[0]
            self.ch = action_page.xpath('//input[@name="ch"]/@value')[0]
            with open(self.sender+'_'+self.type+'_'+self.target['x']
                      + self.target['y']+'.html', 'w') as fd:
                fd.write(r.text.encode('utf-8'))
            return True
        else:
            return False

    def get_post_data(self):
        data = self.troops
        data['x'] = self.target['x']
        data['y'] = self.target['y']
        data[self.type] = 'true'
        data['action_id'] = self.action_id
        data['ch'] = self.ch
        return data

    def send(self, session):
        if self.action_id is None:
            if not self.update_data(session):
                return False
        h = session['h']
        url = 'http://br62.tribalwars.com.br/game.php?village='+self.sender + \
            '&action=command&h='+h+'&screen=place'
        data = self.get_post_data()
        print(data)
        r = requests.post(url, data=data, cookies=session)
        with open('resp.html', 'w') as fd:
            fd.write(r.text.encode('utf-8'))


def getMovement(data):
    sender = data['sender']
    target = data['target']
    type = data['type']
    troops = data['troops']
    return Movement(sender, target, type, troops)
