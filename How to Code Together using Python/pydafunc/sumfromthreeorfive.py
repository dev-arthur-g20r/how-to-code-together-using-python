import os
def sumFromToThreeOrFive(n):
	if (n > 1):
		i = 1
		sum = 0
		while (i <= n):
			if (i % 3 == 0 or i % 5 == 0):
				sum += i
			i += 1
		return "Sum: {}".format(sum)

number = int(input("Number to check its sum from 1 to itself: "))
result = sumFromToThreeOrFive(number)
print(result)
os.system("pause")