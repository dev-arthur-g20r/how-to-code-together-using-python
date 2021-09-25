import os
def lucasSeries(num):
	print "Lucas Series: "
	first = 2
	second = 1
	print "%d" % int(first)
	print "%d" % int(second)
	i = 2
	sum = 0
	while(int(i) < int(num)):
		sum = int(first) + int(second)
		print "%d" % int(sum)
		first = int(second)
		second = int(sum)
		i = int(i) + 1
	return
terms = raw_input("Number of terms: ")
lucasSeries(int(terms))
os.system("pause")