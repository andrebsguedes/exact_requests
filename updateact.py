import json
import requests

cookies = json.load(open('co.json'))
data = json.load(open('troops.json'))
r = requests.post('http://br62.tribalwars.com.br/game.php?village=4833&try=confirm&screen=place', data=data,cookies=cookies)
position = r.text.find('action_id')
start =  position+18
end = start+7
action_id = r.text[start:end]
print(action_id)
data = json.load(open('data.json'))
data['action_id'] = action_id
with open('data.json', 'w') as outfile:
  json.dump(data, outfile)
