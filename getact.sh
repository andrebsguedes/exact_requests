#!/bin/bash
curl  -w "@curl-time.txt" --location --trace-ascii prea.txt --trace-time --data "@troops.txt" -X POST -o ./sideas.html --cookie ./cookies.txt "http://br62.tribalwars.com.br/game.php?village=4833&try=confirm&screen=place" >> file.txt 2>&1
#curl  -w "@curl-time.txt" --location --trace-ascii ea.txt --trace-time --data "@troopsa.txt" -X POST -o ./sidees.html --cookie ./cookies.txt "http://br62.tribalwars.com.br/game.php?village=4833&action=command&h=3290&screen=place" >> file.txt 2>&1
#curl  -w "@curl-time.txt" --trace-ascii d.txt --trace-time --location -w "@curl-time.txt" -o ./side.html -c ./cookies.txt --data "@logindata.txt" -X POST "http://www.tribalwars.com.br/index.php?action=login&server_br62" >> file.txt 2>&1 07:23:25:386
