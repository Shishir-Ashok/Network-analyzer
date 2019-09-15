#!/bin/sh
arp-scan -l -r 2 | tee output1.txt 
sed -i '' '1,2d;N;$!P;$!D;$d' output1.txt
arp -a -n | grep -v "incomplete" | tee output.txt
python parse.py 
