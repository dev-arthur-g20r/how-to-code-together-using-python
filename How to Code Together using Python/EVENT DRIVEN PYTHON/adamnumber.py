import os
def adamNumber(n):
	copy1 = n
	squaren1 = n ** 2
	sum1 = 0
	while (copy1 > 0):
		rem1 = copy1 % 10
		sum1 = (sum1 * 10) + rem1
		copy1 = copy1 // 10
	squaren2 = sum1 ** 2
	copy2 = squaren2
	sum2 = 0
	while (copy2 > 0):
		rem2 = copy2 % 10
		sum2 = (sum2 * 10) + rem2
		copy2 = copy2 // 10
	if (squaren1 == sum2):
		print(n, " is an Adam number.")
	else:
		print(n, " is not an Adam number.")
	return
number = int(input("Number to check if Adam number: "))
adamNumber(number)
os.system("pause")