
fileName = "output1.txt"
fp = open(fileName,"r")

lines = fp.readlines()
# num_lines = sum(1 for line in open(fileName))
# print(num_lines)
i=0
for line in lines:
	
	if(i>=2):

		print(line)
	i = i+1