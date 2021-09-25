import os
def checkGCF(n1,n2):
	while (int(n2) != 0):
		r = int(n1) % int(n2)
		n1 = int(n2)
		n2 = int(r)
	print ("%d is the GCF" % int(n1))
	return
num1 = input("Num1 = ")
num2 = input("Num2 = ")
checkGCF(int(num1),int(num2))
os.system("pause")