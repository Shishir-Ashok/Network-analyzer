
# filename = "IPinfo.txt"
filename = "networkanalyzer/IPinfo.txt"
fp = open(filename,"r")
line = fp.readline()
split = line.split()
IP_Address = split[1]
subnetMask = split[3]
subnetMask = subnetMask[2:]

