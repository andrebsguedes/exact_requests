import subprocess
import sys
import os
import json
timeflag = sys.argv[1]
seconds = int(sys.argv[2])
filename = sys.argv[3]
bashtime = timeflag
res = str(seconds)
if(seconds == 0):
    res = "0000"+res
delay = json.load(open('delay.json'))
time_delay = int(delay['delay'])
if(seconds<time_delay):
    bashtime = bashtime + " -1 minute"
bash = ["at","-f","logger.sh",bashtime]
file_content = "#!/bin/bash\nwait\npython spider.py "+res+" "+filename+" >> file.txt 2>&1"
with open('logger.sh', 'w') as outfile:
    outfile.write(file_content)
process = subprocess.Popen(bash, stdout=subprocess.PIPE, cwd=os.getcwd())
output = process.communicate()[0]
print(output)
