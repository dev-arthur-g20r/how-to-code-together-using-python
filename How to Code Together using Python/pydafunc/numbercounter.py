import os
def numberCounter(n):
	number = str(n)
	zero = 0
	one = 0
	two = 0
	three = 0
	four = 0
	five = 0 
	six = 0
	seven = 0
	eight = 0
	nine = 0
	for i in number:
		if (i == "0"):
			zero += 1
		if (i == "1"):
			one += 1
		if (i == "2"):
			two += 1
		if (i == "3"):
			three += 1
		if (i == "4"):
			four += 1
		if (i == "5"):
			five += 1
		if (i == "6"):
			six += 1
		if (i == "7"):
			seven += 1
		if (i == "8"):
			eight += 1
		if (i == "9"):
			nine += 1
	if (zero > 0):
		print("0 occurred {} times.".format(zero))
	if (one > 0):
		print("1 occurred {} times.".format(one))
	if (two > 0):
		print("2 occurred {} times.".format(two))
	if (three > 0):
		print("3 occurred {} times.".format(three))
	if (four > 0):
		print("4 occurred {} times.".format(four))
	if (five > 0):
		print("5 occurred {} times.".format(five))
	if (six > 0):
		print("6 occurred {} times.".format(six))
	if (seven > 0):
		print("7 occurred {} times.".format(seven))
	if (eight > 0):
		print("8 occurred {} times.".format(eight))
	if (nine > 0):
		print("9 occurred {} times.".format(nine))
number = float(input("Number: "))
numberCounter(number)
os.system("pause")