import os
def triFactor(a,b,c):
	sum = a + b + c
	average = sum / 3
	product = a * b * c
	print("Sum = ", sum)
	print("Average = ", average)
	print("Product = ", product)
	return
num1 = float(input("First number: "))
num2 = float(input("Second number: "))
num3 = float(input("Third number: "))
triFactor(num1,num2,num3)
os.system("pause")