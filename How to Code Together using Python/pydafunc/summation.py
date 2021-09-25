import os
def summation(n,fr,to):
	sum = 0
	i = fr
	while (i <= to):
		sum += n ** i
		i += 1
	return "Summation: {}".format(sum)
number = int(input("Number: "))
fr = int(input("From power: "))
to = int(input("To power: "))
result = summation(number,fr,to)
print(result)
os.system("pause")