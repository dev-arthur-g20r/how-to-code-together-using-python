import os
num = input("Please enter number to check if odd or even: ")
result = int(num) % 2
if (int(result) == 0):
	print ("%d is even." % int(num))
else:
	print ("%d is odd." % int(num))
os.system("pause")