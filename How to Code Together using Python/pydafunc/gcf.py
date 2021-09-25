import os
def gcf(n1,n2):
	while (n2 > 0):
		remainder = n1 % n2
		n1 = n2
		n2 = remainder
	return "GCF: {}".format(n1)
num1 = int(input("Num1: "))
num2 = int(input("Num2: "))
result = gcf(num1,num2)
print(result)
os.system("pause")