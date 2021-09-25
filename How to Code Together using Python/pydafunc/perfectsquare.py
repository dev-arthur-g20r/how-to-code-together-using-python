import os
def isPerfectSquare(n):
	res = 0
	i = 0
	isPerfect = False
	while (i <= 1000):
		res = i ** 2
		if (n == res):
			isPerfect = True
			break
		i += 1
	if (isPerfect):
		return "{} is a perfect square.".format(n)
	else:
		return "{} is not a perfect square.".format(n)
number = int(input("Number to check if perfect square: "))
result = isPerfectSquare(number)
print(result)
os.system("pause")
