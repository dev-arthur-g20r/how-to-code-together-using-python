import os
def lcm(n1,n2):
	if (n1 < n2):
		min = n1
		max = n2
	else:
		min = n2
		max = n1
	i = 1
	while (i <= max):
		checker = max * i
		if (checker % min == 0):
			lcm = checker
			break
		i += 1
	print("LCM:",lcm)
num1 = int(input("Num1 = "))
num2 = int(input("Num2 = "))
lcm(num1,num2)
os.system("pause")