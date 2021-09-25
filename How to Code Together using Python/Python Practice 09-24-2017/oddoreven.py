import os
def oddOrEven(n):
	if (n % 2 == 0):
		return "is EVEN."
	else:
		return "is ODD."
number = int(input("Number to check if odd or even: "))
result = oddOrEven(number)
print(number,result)
os.system("pause")