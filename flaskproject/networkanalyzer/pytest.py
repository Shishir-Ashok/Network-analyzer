fp = open("output1.txt","r")

lines = fp.readlines()
for line in lines:
	IP, MAC, Vendor = line.split('	')
	print(IP)
