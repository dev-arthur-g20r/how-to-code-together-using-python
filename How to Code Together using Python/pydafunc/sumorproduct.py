import os
def sumFromOneTo(n):
	if (n > 1):
		i = 1
		sum = 0
		while (i <= n):
			sum += i
			i += 1
		return "Sum: {}".format(sum)
def productFromOneTo(n):
	if (n > 1):
		i = 1
		product = 1
		while (i <= n):
			product *= i
			i += 1
		return "Product: {}".format(product)

number = int(input("Number to check its sum from 1 to itself: "))
choice = input("+ for Sum or * for Product: ")
if (choice == "+"):
	result = sumFromOneTo(number)
elif (choice == "*"):
	result = productFromOneTo(number)
else:
	result = "Sorry! + or * are only allowed."
print(result)
os.system("pause")