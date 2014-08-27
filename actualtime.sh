curl -w"@curl-time.txt" --trace-ascii trace.txt --trace-time -o side.html -s www.tribalwars.com.br >> file.txt 2>&1
T2="$(date +%H:%M:%S.%N)"
echo "=======">> file.txt 2>&1
echo "Time after: ${T2}">> file.txt 2>&1
echo "+++++++++++++++++++++++++++++++" >> file.txt 2>&1
#T1="$(date +%H:%M:%S.%N)"
#echo "Time before: ${T1}">> file.txt 2>&1

