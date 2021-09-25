import os
def sumFromOneTo(n):
	if (n > 1):
		i = 1
		sum = 0
		while (i <= n):
			sum += i
			i += 1
		return "Sum: {}".format(sum)

number = int(input("Number to check its sum from 1 to itself: "))
result = sumFromOneTo(number)
print(result)
os.system("pause")