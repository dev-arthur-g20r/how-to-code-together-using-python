import os
def checkLCM(n1,n2):
	if (int(n1) > int(n2)):
		max = n1
		min = n2
	else:
		max = n2
		min = n1
	i = 1
	while (int(i) <= int(max)):
		x = int(max) * i
		if (int(x) % int(min) == 0):
			lcd = int(x)
			break
		i = int(i) + 1
	print ("LCM is %d" % int(lcd))
	return
	
num1 = input("Num1 = ")
num2 = input("Num2 = ")
checkLCM(int(num1),int(num2))
os.system("pause")