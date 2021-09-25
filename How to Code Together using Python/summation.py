import os

def checkSummation(number,firstpower,lastpower):
	result = 0
	count = int(firstpower)
	while (int(count) <= int(lastpower)):
		result += int(number) ** int(count)
		count += 1
	print ("Summation: %d" % int(result))
	return

num = input("Number = ")
power_first = input("From first power: ")
power_last = input("To last power: ")
checkSummation(int(num),int(power_first),int(power_last))

os.system("pause")