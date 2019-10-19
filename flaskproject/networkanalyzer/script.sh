#!/bin/sh
arp-scan -l -r 4 | grep -v "DUP" | tee output1.txt 
sed -i '' '1,2d;N;$!P;$!D;$d' output1.txt ;sed -i '' '/^$/d' output1.txt
arp -a -n | grep -v "incomplete" | tee output.txt
ifconfig en0 | grep netmask | tee IPinfo.txt
python getIPinfo.py &
python parse.py &
