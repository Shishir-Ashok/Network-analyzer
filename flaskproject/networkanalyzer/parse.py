def macIP(fileName,getip_filename):
	MACaddressforSearch = []
	MACaddressforSearch[:] = []
	fp = open(getip_filename,"r")
	line = fp.readline()
	split = line.split()
	IP_Address = split[1]
	subnetMask = split[3]
	subnetMask = subnetMask[2:]	
	IP = [] 
	MAC = []
	fp = open(fileName,"r")
	lines = fp.readlines()
	i=1
	#read line by line
	for line in lines:
		#split each line into lists
		split = line.split()
		#store the values of IP and MAC addresses into their respective variables 
		IPaddress = split[1][slice(1,-1)]
		MACaddress = split[3]
		if IP_Address[:7] == IPaddress[:7]:
		#split each MAC address into a list
			macSplit = MACaddress.split(':')
			if(len(MACaddress) != 17):
				n = len(macSplit)
				for item in range (n):
					#if the element in the list is less than 2 characters, add 0 to its begining
					if(len(macSplit[item])!=2):
						macSplit[item] = '0' + macSplit[item]
			macSplit =':'.join(macSplit)
			macSplit = macSplit.upper()

			IP.append(IPaddress)
			MAC.append(macSplit)
			
			macSplit1 = macSplit.replace(':','')
			# print("MACSPLIT1 : ",macSplit1)
			macSplit1 = macSplit1[:6]
			MACaddressforSearch.append(macSplit1)
			# print("IP : %s \tMAC : %s"%(IPaddress,macSplit))	
			i=i+1
	# print("MACaddressforSearch : ",MACaddressforSearch)
	# print(IP, ' ', MAC)
	return IP, MAC, MACaddressforSearch
