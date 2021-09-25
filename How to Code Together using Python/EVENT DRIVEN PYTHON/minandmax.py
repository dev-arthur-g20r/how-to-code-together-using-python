import os
def findMin(thearray):
	min = thearray[0]
	i = 0
	while i < int(len(thearray)):
		if (thearray[i] < min):
			min = thearray[i]
		i = i + 1
	print(min, " is the minimum number in the list.")
	return
def findMax(thearray):
	max = thearray[0]
	i = 0
	while i < int(len(thearray)):
		if (thearray[i] > max):
			max = thearray[i]
		i = i + 1
	print(max, " is the maximum number in the list.")
	return
length = int(input("Number of numbers to determine its minimum and maximum value: "))
numbers = []
i = 0
print("Numbers: ")
while i < length:
	number = int(input(" "))
	numbers.append(number)
	i = i + 1
print(numbers)
findMin(numbers)
findMax(numbers)
os.system("pause")