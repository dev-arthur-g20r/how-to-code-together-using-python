import os
from numericals import Numbers

try:
	number = int(input("Number to check if Harshad: "))
	number_class = Numbers(number)
	print(number_class.isHarshad())
except:
	print("Please enter a number. Sorry but thank you.")

os.system("pause")