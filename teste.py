import datetime
import requests
import json
import sys
from lxml import html
count = False
print(sys.argv[1])
time = int(sys.argv[1])
filename = sys.argv[2]
delay = json.load(open('delay.json'))
time_delay = int(delay['delay'])
if(time < time_delay):
    count = True
else:
    time = time - time_delay
cookies = json.load(open('co.json'))
data = json.load(open(filename))
url = 'http://br62.tribalwars.com.br/game.php?village='+cookies['global_village_id']+'&try=confirm&screen=place'
r = requests.post(url, data=data, cookies=cookies)
with open('first.html', 'w') as fd:
    fd.write(r.text.encode('utf-8'))
action_page = html.fromstring(r.text)
action_id = action_page.xpath('//input[@name="action_id"]/@value')[0]
h_link = action_page.xpath('//*[@id="command-confirm-form"]/@action')[0]
print(h_link)
ch = action_page.xpath('//input[@name="ch"]/@value')[0]
position_h = h_link.find('&h=')
start_h = position_h+3
end_h = start_h+4
h = h_link[start_h:end_h]
print(action_id, h, ch)
url = 'http://br62.tribalwars.com.br/game.php?village='+cookies['global_village_id']+'&action=command&h='+h+'&screen=place'
adata = data
adata['action_id'] = action_id
adata['ch'] = ch
del adata['ca7ab5cbd5a7ec09e35343']
with open('data'+action_id+'.json', 'w') as outfile:
    json.dump(adata, outfile)
if count:
    time = 60000 - time_delay + time
time_s = ((time % 100000) - (time % 1000))/1000
time_us = time % 1000*1000
print(time_s, time_us)
while (datetime.datetime.now().second != time_s or datetime.datetime.now().microsecond <= time_us):
    pass
print(datetime.datetime.now().second, datetime.datetime.now().microsecond)
r = requests.post(url, data=adata, cookies=cookies)
with open('resp.html', 'w') as fd:
    fd.write(r.text.encode('utf-8'))
