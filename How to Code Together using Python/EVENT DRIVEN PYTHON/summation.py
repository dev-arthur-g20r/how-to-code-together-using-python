import os
def summation(number,power1,power2):
	sum = 0
	counter = power1
	while counter <= power2:
		sum += number ** counter
		counter += 1
	print("Summation is ", sum)
	return
	
num = int(input("Number: "))
firstpower = int(input("From the 1st power: "))
lastpower = int(input("To the last power: "))
if (firstpower < lastpower):
	summation(num,firstpower,lastpower)
else:
	print("Sorry! First power should be less than last power.")
os.system("pause")