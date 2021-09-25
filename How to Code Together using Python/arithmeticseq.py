import os
def arithmeticSeq(min,diff,max):
	i = int(min)
	while (int(i) <= int(max)):
		print ("%d" % int(i))
		i = int(i) + diff
	return
	
minimum = input("Minimum: ")
difference = input("Difference: ")
maximum = input("Maximum: ")
arithmeticSeq(int(minimum),int(difference),int(maximum))
os.system("pause")