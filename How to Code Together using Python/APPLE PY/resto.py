import os
def main():
	print("XYZ Restaurant")
	print("Order\t\t\tPrice")
	print("1 - Wine\t\tP200.00")
	print("2 - Cold Drink\t\tP20.00")
	print("3 - Bear\t\tP400.00")
	print("4 - Juice\t\tP100.00")
	print("5 - Exit program")
	pay = 0
	subtotal = 0
	i = 0
	food = []
	price = []
	order = int(input("Choose the number of your order: "))
	choose(order,pay,subtotal,i,food,price)
def choose(order,pay,subtotal,i,food,price):
	if (order == 1):
		subtotal = 200
		pay += subtotal
		i += 1
		print("[",i,"] Wine\t\tP{0:.02f}".format(subtotal))
		price.append(pay)
		food.append("Wine")
		choice = int(input("Order again? (1 if yes or 0 if no.): "))
		if (choice == 1):
			order = int(input("Choose the number of your order: "))
			choose(order,pay,subtotal,i,food,price)
		elif (choice == 0):
			receipt(pay,food,price)
		else:
			print("Invalid input")
	elif (order == 2):
		subtotal = 20
		pay += subtotal
		i += 1
		print("[",i,"] Cold Drink\t\tP{0:.02f}".format(subtotal))
		price.append(pay)
		food.append("Cold Drink")
		choice = int(input("Order again? (1 if yes or 0 if no.): "))
		if (choice == 1):
			order = int(input("Choose the number of your order: "))
			choose(order,pay,subtotal,i,food,price)
		elif (choice == 0):
			receipt(pay,food,price)
		else:
			print("Invalid input")
	elif (order == 3):
		subtotal = 400
		pay += subtotal
		i += 1
		print("[",i,"] Bear\t\tP{0:.02f}".format(subtotal))
		price.append(pay)
		food.append("Bear")
		choice = int(input("Order again? (1 if yes or 0 if no.): "))
		if (choice == 1):
			order = int(input("Choose the number of your order: "))
			choose(order,pay,subtotal,i,food,price)
		elif (choice == 0):
			receipt(pay,food,price)
		else:
			print("Invalid input")
	elif (order == 4):
		subtotal = 100
		pay += subtotal
		i += 1
		print("[",i,"] Juice\t\tP{0:.02f}".format(subtotal))
		price.append(pay)
		food.append("Juice")
		choice = int(input("Order again? (1 if yes or 0 if no.): "))
		if (choice == 1):
			order = int(input("Choose the number of your order: "))
			choose(order,pay,subtotal,i,food,price)
		elif (choice == 0):
			receipt(pay,food,price)
		else:
			print("Invalid input")
	elif (order == 5):
		exit()
	else:
			print("Invalid input")
def receipt(pay,food,price):
	counter = 0
	tax = pay * 0.10
	total = pay + tax
	print("XYZ Restaurant")
	print("Official Receipt")
	print("Order\t\t\tPrice")
	while (counter < len(food) and counter < len(price)):
		print("[",(counter + 1),"]",food[counter],"\t\tP{0:.02f}".format(price[counter]))
		counter += 1
	print("Subtotal: P{0:.02f}".format(pay))
	print("Tax: P{0:.02f}".format(tax))
	print("Total: P{0:.02f}".format(total))
	print("THANK YOU!")
main()
os.system("pause")