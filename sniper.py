import json
import datetime
import sys
import movement
import login


count = False
time = int(sys.argv[1])
filename = sys.argv[2]
delay = json.load(open('delay.json'))
time_delay = int(delay['delay'])
if(time < time_delay):
    count = True
else:
    time = time - time_delay
session = json.load(open('co.json'))
data = json.load(open(filename))
attack = movement.getMovement(data)
if not login.is_logged_in(session):
    session  = login.login()
attack.update_data(session)
#Time shit
if count:
    time = 60000 - time_delay + time
time_s = ((time % 100000) - (time % 1000))/1000
time_us = time % 1000*1000
print(time_s, time_us)
while (datetime.datetime.now().second != time_s or datetime.datetime.now().microsecond <= time_us):
    pass
print(datetime.datetime.now().second, datetime.datetime.now().microsecond)
attack.send(session)
