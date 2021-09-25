import os
your = input("Your currency (P - Philippine Peso, D - US Dollar, Y - Japanese Yen): ")
amount = float(input("Amount of money to convert: "))
if (your == "P" or your == "p"):
	to = input("Convert to (D - US Dollar, Y - Japanese Yen): ")
	if (to == "D" or to == "d"):
		converted = amount / 50.90
		print("PHP {0:0.2f}".format(amount),"converted to USD {0:0.2f}".format(converted))
	elif (to == "Y" or to == "y"):
		converted = amount * 2.19
		print("PHP {0:.2f}".format(amount),"converted to JPY {0:.2f}".format(converted))
	else:
		print("Invalid input")
elif (your == "D" or your == "d"):
	to = input("Convert to (P - Philippine Peso, Y - Japanese Yen): ")
	if (to == "P" or to == "p"):
		converted = amount * 50.90
		print("USD {0:.2f}".format(amount),"converted to PHP {0:.2f}".format(converted))
	elif (to == "Y" or to == "y"):
		converted = amount * 111.29
		print("USD {0:.2f}".format(amount),"converted to JPY {0:.2f}".format(converted))
	else:
		print("Invalid input")
elif (your == "Y" or your == "y"):
	to = input("Convert to (P - Philippine Peso, D - US Dollar): ")
	if (to == "P" or to == "p"):
		converted = amount / 2.19
		print("JPY {0:.2f}".format(amount),"converted to PHP {0:.2f}".format(converted))
	elif (to == "D" or to == "d"):
		converted = amount / 111.29
		print("JPY {0:.2f}".format(amount),"converted to USD {0:.2f}".format(converted))
	else:
		print("Invalid input of choice of currency")
else:
	print("Invalid input of your currency")
os.system("pause")