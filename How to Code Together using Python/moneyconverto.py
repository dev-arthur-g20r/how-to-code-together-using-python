import os
your_currency = input("Enter currency of your money (PHP, USD or JPY): ")
your_money = input("Amount of your money: ")
if(float(your_money) >= 0):
	if (your_currency == "PHP" or your_currency == "php"):
			convert_to = input("Convert to USD or JPY: ")
			if (convert_to == "USD" or convert_to == "usd"):
				converted_money = float(your_money) / 49.52
				print ("Converted money = USD %.2f" % float(converted_money))
			elif (convert_to == "JPY" or convert_to == "jpy"):
				converted_money = float(your_money) * 2.36
				print ("Converted money = JPY %.2f" % float(converted_money))
			else:
				print ("Sorry! Invalid input of currency to be converted to. (USD or JPY only allowed.)")
	elif (your_currency == "USD" or your_currency == "usd"):
			convert_to = input("Convert to PHP or JPY: ")
			if (convert_to == "PHP" or convert_to == "php"):
				converted_money = float(your_money) * 49.52
				print ("Converted money = PHP %.2f" % float(converted_money))
			elif (convert_to == "JPY" or convert_to == "jpy"):
				converted_money = float(your_money) * 117.01
				print ("Converted money = JPY %.2f" % float(converted_money))
			else:
				print ("Sorry! Invalid input of currency to be converted to. (PHP or JPY only allowed.)")
	elif (your_currency == "JPY" or your_currency == "jpy"):
			convert_to = input("Convert to PHP or USD: ")
			if (convert_to == "PHP" or convert_to == "php"):
				converted_money = float(your_money) / 2.36
				print ("Converted money = PHP %.2f" % float(converted_money))
			elif (convert_to == "USD" or convert_to == "usd"):
				converted_money = float(your_money) / 117.01
				print ("Converted money = USD %.2f" % float(converted_money))
			else:
				print ("Sorry! Invalid input of currency to be converted to. (PHP or USD only allowed.)")
	else:
		print ("Sorry! Invalid input of your currency. (PHP, USD and JPY are only allowed to be input as your currency.)")
else:
	print ("Sorry! Money cannot be less than 0.")
os.system("pause")