import os
def lcm(n1,n2):
	if (n1 > n2):
		min = n2
		max = n1
	else:
		min = n1
		max = n2
	i = 1
	while (i <= max):
		product = max * i
		if (product % min == 0):
			lcd = product
			break
		i += 1
	return "LCM: {}".format(lcd)
num1 = int(input("Num1: "))
num2 = int(input("Num2: "))
result = lcm(num1,num2)
print(result)
os.system("pause")