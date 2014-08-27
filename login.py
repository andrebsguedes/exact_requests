import json
import requests
#10574
def login():
    cookies = json.load(open('co.json'))
    data = json.load(open('login.json'))
    proxies = data['proxies']
    del data['proxies']
    r = requests.post('http://www.tribalwars.com.br/index.php?action=login&server_br62', data=data, proxies=proxies)
    cookies['sid'] = r.history[1].cookies['sid']
    cookies['cid'] = r.history[1].cookies['cid']
    cookies['mobile'] = r.cookies['mobile']
    if(data['village'] != ""):
        cookies['global_village_id'] = data['village']
    else:
        cookies['global_village_id'] = r.cookies['global_village_id']
    position_h = r.text.find('&h=')
    start_h = position_h+3
    end_h = start_h+4
    h = r.text[start_h:end_h]
    cookies['h'] = h
    with open('co.json', 'w') as outfile:
      json.dump(cookies, outfile)
    return cookies
    
def is_logged_in(session):
    r = requests.get('http://br62.tribalwars.com.br/game.php?screen=overview', cookies=session)
    if(r.url == 'http://www.tribalwars.com.br/sid_wrong.php'):
        return False
    else:
        return True
