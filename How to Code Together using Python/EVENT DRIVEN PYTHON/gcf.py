import os
def checkGCF(n1,n2):
	while(n2 != 0):
		result = n1 % n2
		n1 = n2
		n2 = result
	print("GCf is ",n1)
	return
num1 = int(input("First number: "))
num2 = int(input("Last number: "))
checkGCF(num1,num2)
os.system("pause")