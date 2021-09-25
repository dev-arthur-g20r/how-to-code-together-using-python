import os
def checkLCM(n1,n2):
	if(n2 > n1):
		min = n1
		max = n2
	else:
		min = n2
		max = n1
	i = 1
	while i <= max:
		x = max * i
		if (x % min == 0):
			lcm = x
			break
		i = i + 1
	print("The LCM is ", lcm)
	return
num1 = int(input("Enter first number: "))
num2 = int(input("Enter last number: "))
checkLCM(num1,num2)
os.system("pause")