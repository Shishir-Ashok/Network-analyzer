import subprocess 
def parseIP(filename):

	fp = open(filename,"r")
	line = fp.readline()
	split = line.split()
	IPaddress = split[1]
	subnetMask = split[3]
	print("IPaddress : {}\tSubnet Mask : {}".format(IPaddress,subnetMask))
	subprocess.call(["sh","test.sh",IPaddress,subnetMask])
if __name__ == '__main__':
	parseIP("IPinfo.txt")
