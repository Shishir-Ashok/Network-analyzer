#!/bin/sh
arp-scan -l -r 5 | tee output1.txt 
sed '1,2d;N;$!P;$!D;$d' output1.txt | tee output2.txt
arp -a -n | grep -v "incomplete" | tee output.txt
python parse.py 
