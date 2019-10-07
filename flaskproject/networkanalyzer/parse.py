MACaddressforSearch = []
def fileParsing(fileName):
	

	fp = open(fileName,"r")

	lines = fp.readlines()

	#print(lines)
	#num_lines = sum(1 for line in open(fileName))
	#print("Number of lines = ",num_lines)
	i=1
	#read line by line
	for line in lines:
		#split each line into lists
		split = line.split()
		#store the values of IP and MAC addresses into their respective variables 
		IPaddress = split[1][slice(1,-1)]
		MACaddress = split[3]

		#split each MAC address into a list
		macSplit = MACaddress.split(':')
		if(len(MACaddress) != 17):
			
			#print(macSplit)
			n = len(macSplit)
			for item in range (n):
				#if the element in the list is less than 2 characters, add 0 to its begining
				if(len(macSplit[item])!=2):
					#print("[ITEM]",macSplit[item])
					macSplit[item] = '0' + macSplit[item]
			#print(macSplit)
			
		macSplit =':'.join(macSplit)
		MACaddressforSearch.append(macSplit.replace(':',''))
		print("IP : %s \tMAC : %s"%(IPaddress,macSplit))
			#print("MACaddressforSearch : ",MACaddressforSearch)	
		i=i+1
	#print("MACaddressforSearch : ",MACaddressforSearch)
if __name__ == "__main__":
	
	fileParsing("output.txt")
	

	# for address in MACaddressforSearch:
	# 	print(address.upper())
