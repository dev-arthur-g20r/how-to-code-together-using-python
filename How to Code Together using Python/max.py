import os
from pprint import pprint
length = input("Number of numbers for checking maxmimum value: ")
i = 0
numbers = []
print ("Numbers: ")
while (int(i) < int(length)):
	n = input(" ")
	numbers.append(int(n))
	i = int(i) + 1
min_result = min(numbers)
max_result = max(numbers)
pprint(numbers)
print ("Sorted array: ") 
numbers.sort()
pprint(numbers)
print ("Minimum number is: %d" % int(min_result))
print ("Maximum number is: %d" % int(max_result))
os.system("pause")