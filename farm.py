import login
import json
import movement
import sys
import threading


class myThread (threading.Thread):
    def __init__(self, threadID, name, attack, session):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.attack = attack
        self.session = session

    def run(self):
        print self.threadID, self.name
        self.attack.send(self.session)


def farm(session, sender, targets, troops_template):
    threads = []
    counter = 1
    for target in targets:
        attack = movement.Movement(sender, target, 'attack', troops_template)
        thread = myThread(counter, target['x']+"|"+target['y'], attack,
                          session)
        threads.append(thread)
        counter = counter + 1
    for thread in threads:
        thread.start()
    return threads

sender = sys.argv[1]
targets = json.load(open(sys.argv[2]))
troops = json.load(open(sys.argv[3]))
session = json.load(open('co.json'))
if not login.is_logged_in(session):
    session = login.login()
farm(session, sender, targets, troops)
