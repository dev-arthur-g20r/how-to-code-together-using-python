import os
def sort(n1,n2,n3):
	numbers = [n1, n2, n3]
	minimum = min(numbers)
	maximum = max(numbers)
	mid = (n1 + n2 + n3) - (minimum + maximum)
	print (minimum, ", ", mid, ", ", maximum)
	return
num1 = int(input("Num1: "))
num2 = int(input("Num2: "))
num3 = int(input("Num3: "))
sort(num1,num2,num3)
os.system("pause")
